from PyQt5 import QtWidgets

from gui.compiled.compiled_Form_Login import Ui_Form_Login


class FormLogin(QtWidgets.QWidget, Ui_Form_Login):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()

    def set_up_initial(self):
        pass