import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QTimer
from PyQt5.QtGui import QPixmap, QImage

from gui.compiled.compiled_Form_Camera import Ui_Form_Camera
from gui.item_medication import MedicationItem


class FormCamera(QtWidgets.QWidget, Ui_Form_Camera):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.timer = QTimer(self)
        self.cap = cv2.VideoCapture(0)
        self.set_up_initial()

    def set_up_initial(self):
        self.timer.timeout.connect(self.update_frame)
        self.layout_medi_list.addWidget(MedicationItem(self.controller, "타이레놀 서방정 650mg"))
        self.layout_medi_list.addWidget(MedicationItem(self.controller, "트윈스타정 25mg"))
        self.layout_medi_list.addWidget(MedicationItem(self.controller, "가스터 10mg"))

    def start_update_image(self):
        self.timer.start(60)

    def stop_update_image(self):
        self.timer.stop()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def update_frame(self):
        if not self.cap.isOpened():
            return
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB format for QImage
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame_rgb.shape
            bytes_per_line = 3 * width
            q_image = QImage(frame_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.label_camera.setPixmap(pixmap)

    def closeEvent(self, event):
        self.cap.release()

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        height, width, channel = rgb_image.shape
        bytes_per_line = width * channel
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
