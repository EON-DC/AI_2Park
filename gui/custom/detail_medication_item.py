import pandas as pd
from PyQt5 import QtGui, QtWidgets

from gui.compiled.compiled_detail_medication_item import Ui_Detail_Item
from gui.form_schedule_checking import FormCheckingSchedule
from gui.form_schedule_taking import FormTakingSchedule


class DetailMedicationItem(QtWidgets.QWidget, Ui_Detail_Item):

    def __init__(self, parent=None, controller=None, medication:pd.DataFrame=None, prescription: pd.Series = None):
        super().__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.medication = medication
        self.prescription = prescription  # series
        self.form_taking = None
        self.form_checking = None
        self.set_up_initial()

    def set_controller(self, controller):
        self.controller = controller

    def set_up_initial(self):
        self.label_medi_name.setText(self.medication["dl_name"][0])
        self.label_class_no.setText(self.medication["di_class_no"][0])
        self.label_etc_otc.setText(self.medication["di_etc_otc_code"][0])
        self.btn_taking_schedule.clicked.connect(lambda state: self.create_from_taking_schedule())
        self.btn_checking_schedule.clicked.connect(lambda state: self.create_form_checking_schedule())

    def create_from_taking_schedule(self):
        self.form_taking = FormTakingSchedule(self.controller, self.medication, self.prescription)
        self.form_taking.exec_()

    def create_form_checking_schedule(self):
        self.form_checking = FormCheckingSchedule(self.controller, self.medication, self.prescription)
        self.form_checking.exec_()


    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("클릭된 정보", self.prescription, self.medication)
