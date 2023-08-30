from multiprocessing import Process

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication

from gui.compiled.compiled_form_loader import Ui_Form_Loader


def run_loading_widget(sys_argv):
    app = QApplication(sys_argv)
    window = FormLoader()
    window.show()
    app.exec_()

class LoaderPage(QtWidgets.QWidget):
    def __init__(self, sys_argv):
        self.process = Process(target=run_loading_widget, args=(sys_argv,))
        self.process.start()
class FormLoader(QtWidgets.QWidget, Ui_Form_Loader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(600,150,400,400)
        self.setWindowFlags(self.windowFlags())
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.movie = QMovie(":/image/pill_loader.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.show()
    def finished_loading(self):
        self.close()
