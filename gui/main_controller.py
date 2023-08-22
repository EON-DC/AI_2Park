from PyQt5 import QtCore, QtGui, QtWidgets
from gui.compiled.compiled_MainApp import Ui_MainApp
from database.db_connector import DBConnector
from gui.form_camera import FormCamera


class UIController(QtWidgets.QWidget, Ui_MainApp):

    def __init__(self, db_conn: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.db_conn = db_conn
        self.form_camera = FormCamera()
        self.set_up_initial()

    def set_up_initial(self):
        self.stackedWidget.setCurrentIndex(0)
        self.layout_page_1.addWidget(self.form_camera)



    @staticmethod
    def show_error_message(message, traceback):
        # error message 메세지 박스 띄워주기
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()
