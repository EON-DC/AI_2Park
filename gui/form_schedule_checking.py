from PyQt5 import QtWidgets

from gui.compiled.compiled_checking_schedule import Ui_FormCheckingSchedule


class FormCheckingSchedule(QtWidgets.QDialog, Ui_FormCheckingSchedule):
    def __init__(self, main_controller, medication, prescription):
        super().__init__()
        self.controller = main_controller
        self.medication = medication
        self.prescription = prescription
        self.setupUi(self)
        self.set_up_initial()

    def set_up_initial(self):
        pass