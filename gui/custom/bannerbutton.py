from PyQt5.QtCore import QSize, QRect, QPropertyAnimation
from PyQt5.QtWidgets import QPushButton


class BannerButton(QPushButton):
    banner_default_geometry = QRect(100, 10, 160, 60)
    banner_hovered_geometry = QRect(20, 10, 160, 60)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(self.banner_default_geometry)
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(600)  # 200 milliseconds

    def enterEvent(self, event):
        super().enterEvent(event)
        self.start_animation("enter")

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.start_animation("leave")

    def start_animation(self, command):
        """ Start the size animation """
        if command == "enter":
            start_rect = self.banner_default_geometry
            end_rect = self.banner_hovered_geometry

        else:
            start_rect = self.banner_hovered_geometry
            end_rect = self.banner_default_geometry

        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()
