import pickle
import traceback

import PIL
import cv2
import numpy as np
import pandas as pd
import ultralytics.engine.results
import yaml
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
        self.detection_model = YOLO(r"model/object_detection.pt")
        self.circle_classification_model = YOLO(r"model/circle_classification.pt")
        self.ellipse_classification_model = YOLO(r"model/ellipse_classification.pt")
        self.cap = cv2.VideoCapture(0)
        # self.pretrained_model = keras.models.load_model(r"model/model_test.h5")
        self.predicted_medication_mapping_list = list()
        self.temp_medi_df = pd.DataFrame()
        self.finished_signal.emit()
        self.circle_dict, self.ellipse_dict = self.yaml_loader()
        self.set_up_initial()

    def set_up_initial(self):
        self.timer.timeout.connect(self.update_frame)
        self.label_camera_guide.setVisible(False)

    def yaml_loader(self):
        with open("model/cls_circle.yaml", 'r', encoding='utf-8') as file:
            circle_dict = yaml.safe_load(file, )

        with open("model/cls_ellipse.yaml", 'r', encoding='utf-8') as file:
            ellipse_dict = yaml.safe_load(file, )
        return circle_dict, ellipse_dict

    def get_mapping_code_from_yaml(self, cls_num, shape_type):
        if shape_type == "ellipse":
            return "K-0" + self.ellipse_dict["names"][cls_num]
        elif shape_type == "circle":
            return "K-0" + self.circle_dict["names"][cls_num]

    def start_update_image(self):
        self.timer.start(120)

    def stop_update_image(self):
        self.timer.stop()

    # 감지 모델을 불러오는 것
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            result = self.detection_model.predict(source=frame, show=False, stream=False, conf=0.4, verbose=False)
            try:
                self.displayImage(result)
            except:
                # traceback.print_exc()
                pass

    def displayImage(self, frame):
        frame: ultralytics.engine.results.Results
        snapshot = frame[0]
        boxes_data = snapshot.boxes
        if len(boxes_data.cls) > 0:
            orig_img = snapshot.orig_img
            for cls_ in boxes_data.cls:
                if int(cls_) == 0:  # 원형
                    result = self.circle_classification_model.predict(source=orig_img, show=False, stream=False,
                                                                      conf=0.6, verbose=False)
                    is_circle = True
                else:
                    result = self.ellipse_classification_model.predict(source=orig_img, show=False, stream=False,
                                                                       conf=0.6, verbose=False)
                    is_circle = False
                inner_boxes = result[0].boxes
                inner_boxes: ultralytics.engine.results.Boxes
                class_list = inner_boxes.cls
                confidence_list = inner_boxes.conf

                for cls_tensor, conf_, in zip(class_list, confidence_list):
                    class_number = cls_tensor.item()
                    print("is_circle=", is_circle, "confidence=", conf_.item())
                    if conf_.item() < 0.9:
                        self.label_camera_guide.setVisible(True)
                        continue
                    self.label_camera_guide.setVisible(False)
                    if is_circle:
                        mapping_code = self.get_mapping_code_from_yaml(class_number, "circle")
                    else:
                        mapping_code = self.get_mapping_code_from_yaml(class_number, "ellipse")
                    print("mapping_code= ", mapping_code)
                    if mapping_code in self.predicted_medication_mapping_list:
                        continue
                    if self.verify_same_medication(mapping_code):
                        continue
                    self.add_medication_list(mapping_code)
                    medi_df_row = self.controller.db_conn.find_medication_by_mapping_code(mapping_code)
                    self.temp_medi_df = pd.concat([self.temp_medi_df, medi_df_row], ignore_index=True)
                    # self.temp_medi_df.reset_index(inplace=True)
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

    def remove_medication_list(self, mapping_code):
        self.predicted_medication_mapping_list.remove(mapping_code)
        self.refresh_medication_count()

    def verify_same_medication(self, mapping_code):
        mapping_code = "K-" + f"{mapping_code}"
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
