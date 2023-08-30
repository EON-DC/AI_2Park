import os

import pandas as pd
import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize

from database.db_connector import DBConnector
from gui.compiled.compiled_MainApp import Ui_MainApp
from gui.form_camera import FormCamera
from gui.form_home import FormHome
from gui.form_login import FormLogin
from gui.form_medi_detail import FormMedicationDetails
from gui.form_saved_list import FormSavedList


class UIController(QtWidgets.QWidget, Ui_MainApp):

    def __init__(self, db_conn: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(450, 80, self.width(), self.height())
        self.setWindowFlags(self.windowFlags())
        self.db_conn = db_conn
        self.form_camera = FormCamera(self)
        self.form_camera.finished_signal.connect(self.close_form_loading)
        self.form_login = FormLogin(self)
        self.form_saved_list = FormSavedList(self)
        self.form_home = FormHome(self)
        self.form_detail = FormMedicationDetails(self)
        self.user_df = None
        self.selected_prescription_df = pd.DataFrame()
        self.set_up_initial()

    def set_up_initial(self):
        # signal
        self.hide_title(True)
        self.stackedWidget.setCurrentIndex(0)
        self.layout_page_0.addWidget(self.form_login)
        self.layout_page_1.addWidget(self.form_home)
        self.layout_page_2.addWidget(self.form_camera)
        self.layout_page_3.addWidget(self.form_saved_list)
        self.layout_page_4.addWidget(self.form_detail)
        self.label_locker.clicked.connect(lambda: self.set_page("logout"))
        self.btn_banner_1.clicked.connect(lambda state: self.set_page("camera"))
        self.btn_banner_2.clicked.connect(lambda state: self.set_page("saved_list"))
        self.btn_banner_3.clicked.connect(lambda state: self.set_page("home"))
        self.btn_banner_4.clicked.connect(lambda state: self.set_page("detail_list"))

        self.get_app_config()

    def set_page(self, command):
        # 혹시 카메라 켜져있으면 끄기
        self.form_camera.stop_update_image()
        command_list = ["camera", "saved_list", "detail_list", "home", "login", "logout"]
        if command not in command_list:
            raise "커맨드 입력 확인"
        elif command == "logout":
            self.hide_title(True)
            self.stackedWidget.setCurrentIndex(0)
            self.get_app_config()
            # 저장 정보 비우기
            self.user_df.drop(self.user_df.index)
            self.selected_prescription_df.drop(self.selected_prescription_df.index)
        elif command == "home":
            self.label_section_title.setText("프로그램 소개")
            self.stackedWidget.setCurrentIndex(1)
        elif command == "camera":
            self.label_section_title.setText("실시간 약물 분류")
            self.stackedWidget.setCurrentIndex(2)
            self.form_camera.start_update_image()
        elif command == "saved_list":
            self.label_section_title.setText("저장 복용 리스트")
            self.form_saved_list.refresh_list_widget()
            self.stackedWidget.setCurrentIndex(3)
        elif command == "detail_list":
            self.label_section_title.setText("실시간 분류된 경구약 상세정보")
            self.form_detail.refresh_list_widget()
            self.stackedWidget.setCurrentIndex(4)

    def enter_banner(self, btn, enter_state):
        if enter_state is True:
            btn.setGeometry(self.banner_hovered_geometry)
        else:
            btn.setGeometry(self.banner_default_geometry)

    def login_success(self, user_df: pd.DataFrame):
        self.user_df = user_df
        print("로그인 되었습니다. 로그인 정보:")
        print(user_df)
        self.label_user_info.setText(f"{user_df['name'][0]}님, 안녕하세요.")
        self.form_login.clear_line_edit()
        self.set_page("home")
        self.hide_title(False)
        self.update_app_config()

    def hide_title(self, command):
        login_window_size = QSize(980, 700)
        default_window_size = QSize(1130, 800)

        if command is True:
            self.resize(login_window_size)
            self.widget_header.setVisible(False)
            self.banner.setVisible(False)

        else:
            self.resize(default_window_size)
            self.widget_header.setVisible(True)
            self.banner.setVisible(True)

    def get_app_config(self):
        current_path = os.getcwd()
        with open(f"{current_path}\\gui\\app_config.yaml", "r", encoding="utf-8") as f:
            list_doc = yaml.safe_load(f)

        if list_doc["set_username_remember"] is False:
            self.form_login.checkBox.setChecked(False)
        else:
            self.form_login.checkBox.setChecked(True)
            self.form_login.lineEdit_username.setText(list_doc["remember_username"])

    def update_app_config(self):
        current_path = os.getcwd()
        with open(f"{current_path}\\gui\\app_config.yaml", "r", encoding="utf-8") as f:
            list_doc = yaml.safe_load(f)

        if self.form_login.checkBox.isChecked() is True:
            list_doc["set_username_remember"] = True
            list_doc["remember_username"] = f"{self.user_df.iloc[0]['username']}"
        else:
            list_doc["set_username_remember"] = False

        with open(f"{current_path}\\gui\\app_config.yaml", "w", encoding="utf-8") as f:
            yaml.safe_dump(list_doc, f)

    @staticmethod
    def clear_widget(widget: QtWidgets.QWidget):
        layout_ = widget.layout()
        while layout_.count():
            item = layout_.takeAt(0)
            item.widget().deleteLater()

    @staticmethod
    def show_error_message(message, traceback):
        # error message 메세지 박스 띄워주기
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()

    def close_form_loading(self):
        self.form_loader.finished_loading()
