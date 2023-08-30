from PyQt5 import QtWidgets

from gui.compiled.compiled_widget_checking_row import Ui_Widget_Checking_Row


class CheckingRow(QtWidgets.QWidget, Ui_Widget_Checking_Row):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
