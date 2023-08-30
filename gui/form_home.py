from PyQt5 import QtWidgets

from gui.compiled.compiled_Form_Home import Ui_Form_Home


class FormHome(QtWidgets.QWidget, Ui_Form_Home):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()

    def set_up_initial(self):
        pass
