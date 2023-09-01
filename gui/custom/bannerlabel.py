from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QLabel


class BannerLabel(QLabel):
    # 클릭이벤트 설정
    clicked = pyqtSignal()

    hovered_style = """
        QLabel{
            border: 2px solid #DFDFDF;
        }
    """
    default_style = """
        QLabel{
            border: 2px solid #FFFFFF;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        # property gif movie
        # 자물쇠 lock으로 셋팅
        self.locked_image = QPixmap(":/image/img_lock.png")
        self.unlocked_image = QPixmap(":/image/img_unlock.png")
        self.movie_lock = QMovie(":/image/lock.gif")
        self.movie_unlock = QMovie(":/image/unlock.gif")
        self.setPixmap(self.unlocked_image)
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setStyleSheet(self.hovered_style)
        self.setMovie(self.movie_lock)
        self.movie_lock.start()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setStyleSheet(self.default_style)
        self.movie_lock.stop()
        self.setPixmap(self.unlocked_image)

    def mousePressEvent(self, event):
        self.clicked.emit()
