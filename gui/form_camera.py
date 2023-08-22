import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap

from gui.camera_reader import WebCamViewer
from gui.compiled.compiled_Form_Camera import Ui_Form_Camera
from gui.item_medication import MedicationItem


class FormCamera(QtWidgets.QWidget, Ui_Form_Camera):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread = WebCamViewer()
        self.set_up_initial()

    def set_up_initial(self):
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()

        self.layout_medi_list.addWidget(MedicationItem("타이레놀 서방정 650mg"))
        self.layout_medi_list.addWidget(MedicationItem("트윈스타정 25mg"))
        self.layout_medi_list.addWidget(MedicationItem("가스터 10mg"))

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)