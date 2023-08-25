from PyQt5 import QtCore, QtGui, QtWidgets
from gui.compiled.compiled_medi_item import Ui_Widget_Medi_Item


class MedicationItem(QtWidgets.QWidget, Ui_Widget_Medi_Item):

    def __init__(self, main_controller, medication_name):
        super().__init__()
        self.setupUi(self)
        self.controller = main_controller
        self.medication = medication_name
        self.set_up_initial()

    def set_up_initial(self):
        self.label_medi_name.setText(self.medication)
        self.btn_delete.clicked.connect(lambda state: self.btn_delete_clicked())

    def btn_delete_clicked(self):
        # todo: in-memory 선택 약물 삭제 로직 추가
        self.deleteLater()

