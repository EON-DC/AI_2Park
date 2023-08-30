import pickle

import PIL
import cv2
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from ultralytics import YOLO

from gui.compiled.compiled_Form_Camera import Ui_Form_Camera
from gui.custom.detected_item import DetectedItem


class FormCamera(QtWidgets.QWidget, Ui_Form_Camera):
    finished_signal = pyqtSignal()

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.timer = QTimer(self)
        self.detection_model = YOLO(r"model/best.pt")
        self.cap = cv2.VideoCapture(0)
        # self.pretrained_model = keras.models.load_model(r"model/model_test.h5")
        self.pretrained_model = None
        self.predicted_medication_mapping_list = list()
        self.temp_medi_df = pd.DataFrame()
        self.set_up_initial()
        self.finished_signal.emit()

    def set_up_initial(self):
        self.timer.timeout.connect(self.update_frame)

    def start_update_image(self):
        self.timer.start(120)

    def stop_update_image(self):
        self.timer.stop()

    # 감지 모델을 불러오는 것
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = self.detection_model.predict(source=frame, show=False, stream=False, conf=0.93, verbose=False)
            try:
                self.displayImage2(frame)
            except:
                pass

    def displayImage(self, img, boxes_data):
        qformat = QImage.Format_RGB888
        img = QImage(img, img.shape[1], img.shape[0], qformat)
        img = img.rgbSwapped()  # Convert BGR to RGB
        self.label_camera.setPixmap(QPixmap.fromImage(img))

    def displayImage2(self, frame):
        boxes = frame[0].boxes
        if len(boxes.cls) > 0:
            boxes_data = boxes.data
            orig_img = frame[0].orig_img.copy()
            fix_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2RGB)
            _, crop_img = self.draw_boxes_and_crop(fix_img, boxes_data)
            for idx, cropped_img in enumerate(crop_img):
                alpha_channel = np.ones(cropped_img.shape[:2], dtype=cropped_img.dtype) * 255
                four_channel_img = cv2.merge([cropped_img, alpha_channel])
                cropped_img = PIL.Image.fromarray(four_channel_img)
                img = cropped_img.resize((32, 32))
                img = np.array(img)
                img_list = [img]
                img_list = np.array(img_list)
                # result = self.pretrained_model.predict(np.array(img_list), verbose=0)
                result = np.array([[ 5.1012e-09,  3.7004e-11,           1]])
                predict_result = np.round(result)
                predict_classes = predict_result.argmax(axis=1)
                with open(r"model/labelencoder.pickle", "rb") as file:
                    encoder = pickle.load(file)
                    orgin_labels = encoder.inverse_transform(predict_classes)
                    # 분류 모델을 불러오는 것
                    for mapping_code in orgin_labels:
                        mapping_code = 22074  # todo : 나중에 바꾸기
                        if mapping_code in self.predicted_medication_mapping_list:
                            continue
                        if self.verify_same_medication(mapping_code):
                            continue
                        self.add_medication_list(mapping_code)
                        medi_df_row = self.controller.db_conn.find_medication_by_mapping_code(mapping_code)
                        self.temp_medi_df = pd.concat([self.temp_medi_df, medi_df_row])
                        self.temp_medi_df.reset_index(inplace=True)
                        self.layout_medi_list.addWidget(DetectedItem(self, self.controller, medi_df_row))
        try:
            img = frame[0].plot()
            qformat = QImage.Format_RGB888
            img = QImage(img, img.shape[1], img.shape[0], qformat)
            img = img.rgbSwapped()  # Convert BGR to RGB
            self.label_camera.setPixmap(QPixmap.fromImage(img))
        except:
            pass

    def add_medication_list(self, mapping_code):
        self.predicted_medication_mapping_list.append(mapping_code)
        self.refresh_medication_count()

    def verify_same_medication(self, mapping_code):
        try:
            result = self.controller.selected_prescription_df[
                self.controller.selected_prescription_df["dl_mapping_code"] == mapping_code]
        except:
            return False

        if len(result) > 0:
            return True
        return False

    def closeEvent(self, event):
        self.cap.release()

    def refresh_medication_count(self):
        origin = f"현재까지 {len(self.predicted_medication_mapping_list)}종 약물이 확인되었습니다." + \
                 f"\n저장된 약물은 {len(self.controller.selected_prescription_df)}건입니다."
        self.label_status.setText(origin)

    @staticmethod
    def draw_boxes_and_crop(image, tensor):
        cropped_images = []
        for detection in tensor:
            x1, y1, x2, y2 = map(int, detection[:4])
            confidence = detection[4]
            class_id = int(detection[5])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Class {class_id} : {confidence:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cropped = image[y1:y2, x1:x2]
            cropped_images.append(cropped)
        return image, cropped_images

    # TODO: 추가할 일

    # 분류 모델이 분류하는대로 라벨을 추가하는 로직
