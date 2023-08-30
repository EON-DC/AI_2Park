from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox

from gui.compiled.compiled_Dialog_Join import Ui_Dialog_Join
from gui.dialog_rules import DialogRules


class DialogJoin(QtWidgets.QDialog, Ui_Dialog_Join):
    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.dialog_rules = None
        self.has_username_valid = False
        self.set_up_initial()

    def set_up_initial(self):
        self.btn_join.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.label_guide.setVisible(False)
        self.btn_rules.clicked.connect(lambda state: self.create_rules_dialog())
        self.btn_valid_username.clicked.connect(lambda state: self.valid_same_username())
        self.lineEdit_username.textChanged.connect(lambda text: self.change_need_to_valid())
        self.btn_join.clicked.connect(lambda state: self.try_join())

    def change_need_to_valid(self):
        self.has_username_valid = False
        self.btn_valid_username.setEnabled(True)

    def valid_same_username(self):
        self.label_guide.setVisible(True)
        input_username = self.lineEdit_username.text()
        has_same_name = self.controller.db_conn.check_duplicate_username(input_username)
        if has_same_name is True:
            self.label_guide.setText("이미 사용중인 아이디입니다.")
            self.set_label_guide_color("red")
        else:
            self.label_guide.setText("사용가능한 아이디입니다.")
            self.set_label_guide_color("blue")
            self.has_username_valid = True
            self.btn_valid_username.setEnabled(False)

    def create_rules_dialog(self):
        self.dialog_rules = DialogRules(self, self.controller)
        result = self.dialog_rules.exec_()
        if result == QDialog.Accepted:
            self.checkBox.setChecked(True)
            self.btn_join.setEnabled(True)

    def set_label_guide_color(self, command):
        if command == "blue":
            self.label_guide.setStyleSheet("QLabel { color : #86AEEF; }")
        else:
            self.label_guide.setStyleSheet("QLabel { color : #E8864A; }")

    def valid_all_edit_line(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        name = self.lineEdit_name.text()
        email = self.lineEdit_email.text()
        check_list = {"아이디": username, "비밀번호": password, "이름": name, "이메일": email}
        for k, v in check_list.items():
            if len(v) == 0:
                self.label_guide.setText(f"{k}을 작성해주세요.")
                self.set_label_guide_color("red")
                return False
        if self.btn_valid_username.isEnabled() is True:
            self.label_guide.setText(f"중복 확인을 해주세요.")
            self.set_label_guide_color("red")
            return False
        return True

    def try_join(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        name = self.lineEdit_name.text()
        email = self.lineEdit_email.text()

        valid_result = self.valid_all_edit_line()
        if valid_result is False:
            return
        join_result = self.controller.db_conn.join(username, password, name, email)
        if join_result is False:
            self.label_guide.setText(f"시스템 상으로 현재 가입이 불가능합니다. \n 오류 보고 또는 잠시후 시행해주십시요.")
            self.set_label_guide_color("red")
            return
        QMessageBox.about(self, "안내", "회원가입이 되었습니다.")
        self.close()

