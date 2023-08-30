from PyQt5 import QtWidgets

from gui.compiled.compiled_Form_Login import Ui_Form_Login
from gui.dialog_join import DialogJoin


class FormLogin(QtWidgets.QWidget, Ui_Form_Login):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()
        self.dialog_join = None

    def set_up_initial(self):
        self.label_guide.setVisible(False)
        self.lineEdit_password.returnPressed.connect(lambda :self.try_login())
        self.btn_join.clicked.connect(lambda state: self.create_join_page())
        self.btn_login.clicked.connect(lambda state: self.try_login())

    def try_login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        login_result = self.controller.db_conn.access_login(username, password)
        if login_result is False:
            self.label_guide.setText("잘못된 회원정보입니다. 다시 시도해주세요.")
            self.set_label_guide_color("red")
            return
        self.controller.login_success(login_result)  # 회원 정보 dataframe 전달

    def create_join_page(self):
        self.dialog_join = DialogJoin(self.controller)
        self.dialog_join.exec_()

    def set_label_guide_color(self, command):
        self.label_guide.setVisible(True)
        if command == "blue":
            self.label_guide.setStyleSheet("QLabel { color : #86AEEF; }")
        else:
            self.label_guide.setStyleSheet("QLabel { color : #E8864A; }")


    def clear_line_edit(self):
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()
        self.label_guide.setVisible(False)
