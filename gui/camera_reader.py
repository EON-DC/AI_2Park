import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal


class WebCamViewer(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.webcam = None

    def turn_on_cam(self):
        if self.webcam is None:
            self.webcam = cv2.VideoCapture(0)

    def get_cam_image(self):
        status, frame = self.webcam.read()
        if status:
            # cv2.imshow("test", frame)
            self.change_pixmap_signal.emit(frame)

    def turn_off_cam(self):
        self.webcam.release()
        self.webcam = None
        # cv2.destroyAllWindows()

    def check_cam_state(self):
        if not self.webcam.isOpened():
            return False
        return True
