from PyQt5 import QtWidgets

from gui.compiled.compiled_Dialog_Rules import Ui_Dialog_rule


class DialogRules(QtWidgets.QDialog, Ui_Dialog_rule):
    def __init__(self, dialog_join, main_controller):
        super().__init__()
        self.dialog_join = dialog_join
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()

    def set_up_initial(self):
        self.btn_ok.clicked.connect(self.accept)

