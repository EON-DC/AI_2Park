from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QMovie
from gui.compiled.compiled_MainApp import Ui_MainApp
from database.db_connector import DBConnector
from gui.form_camera import FormCamera
from gui.form_login import FormLogin


class UIController(QtWidgets.QWidget, Ui_MainApp):

    def __init__(self, db_conn: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.db_conn = db_conn
        self.form_camera = FormCamera(self)
        self.form_login = FormLogin(self)

        self.set_up_initial()

    def set_up_initial(self):
        self.stackedWidget.setCurrentIndex(0)
        self.layout_page_1.addWidget(self.form_camera)
        self.layout_page_3.addWidget(self.form_login)
        self.btn_banner_1.clicked.connect(lambda state: self.set_page("camera"))
        self.btn_banner_2.clicked.connect(lambda state: self.set_page("saved_list"))

    def set_page(self, command):
        if command == "camera":
            self.label_section_title.setText("실시간 약물 분류")
            self.stackedWidget.setCurrentIndex(0)
        elif command == "saved_list":
            self.label_section_title.setText("저장 복용 리스트")
            self.stackedWidget.setCurrentIndex(1)
        elif command == "login":
            self.label_section_title.setText("로그인")
            self.stackedWidget.setCurrentIndex(4)


    def enter_banner(self, btn, enter_state):
        if enter_state is True:
            btn.setGeometry(self.banner_hovered_geometry)
        else:
            btn.setGeometry(self.banner_default_geometry)

    @staticmethod
    def show_error_message(message, traceback):
        # error message 메세지 박스 띄워주기
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()
