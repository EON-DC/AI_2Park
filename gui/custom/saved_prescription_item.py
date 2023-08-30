import pandas as pd
from PyQt5 import QtGui, QtWidgets

from gui.compiled.compiled_saved_prescription_item import Ui_Saved_Prescription_Item
from gui.form_schedule_taking import FormTakingSchedule


class SavedPrescriptionItem(QtWidgets.QWidget, Ui_Saved_Prescription_Item):
    """
    데이터베이스에서 저장된 처방을 불러와서 보여주는 네모 위젯
    """

    def __init__(self, parent=None, controller=None, prescription: pd.Series = None, medication:pd.DataFrame=None):
        super().__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.prescription = prescription  # series
        self.medication = medication
        self.form_taking = None
        self.set_up_initial()

    def set_controller(self, controller):
        self.controller = controller

    def set_up_initial(self):
        self.label_medi_name.setText(f"{self.medication['dl_name'][0]}")
        self.label_saved_time.setText(f"저장일시: {self.prescription['saved_timestamp']}")
        self.label_start_date.setText(f"복용시작일: {self.prescription['taking_start_timestamp']}")
        self.label_medi_amount.setText(f"복용량: {self.prescription['eat_amount']}tab")
        self.label_day_duration.setText(f"복용기간: {self.prescription['day_duration']}일")
        self.label_daily_count.setText(f"하루복용횟수: {self.prescription['daily_eat_count']}회")
        # todo set label image 로직 추가

        self.btn_edit.clicked.connect(lambda state: self.create_from_taking_schedule())

    def create_from_taking_schedule(self):
        self.form_taking = FormTakingSchedule(self.controller, self.medication, self.prescription)
        self.form_taking.exec_()

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("클릭된 정보", self.prescription, self.medication)
