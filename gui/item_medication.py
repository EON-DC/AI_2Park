from PyQt5 import QtCore, QtGui, QtWidgets
from gui.compiled.compiled_medi_item import Ui_Widget_Medi_Item


class MedicationItem(QtWidgets.QWidget, Ui_Widget_Medi_Item):

    def __init__(self, medication_name):
        super().__init__()
        self.setupUi(self)
        self.medication = medication_name
        self.set_up_initial()

    def set_up_initial(self):
        self.label_medi_name.setText(self.medication)
