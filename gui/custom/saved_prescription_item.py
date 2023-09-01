import traceback

import pandas as pd
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QByteArray
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from gui.compiled.compiled_saved_prescription_item import Ui_Saved_Prescription_Item
from gui.form_schedule_checking import FormCheckingSchedule
from gui.form_schedule_taking import FormTakingSchedule


class SavedPrescriptionItem(QtWidgets.QWidget, Ui_Saved_Prescription_Item):
    """
    데이터베이스에서 저장된 처방을 불러와서 보여주는 네모 위젯
    """

    def __init__(self, parent=None, controller=None, prescription: pd.Series = None, medication: pd.DataFrame = None):
        super().__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.prescription = prescription  # series
        self.medication = medication
        self.form_taking = None
        self.form_checking = None
        self.set_up_initial()

    def set_controller(self, controller):
        self.controller = controller

    def set_up_initial(self):
        self.label_medi_name.setText(f"{self.medication['dl_name'][0]}")
        self.label_saved_time.setText(f"최초저장일시:\n{self.prescription['saved_timestamp'].strftime('%Y-%m-%d %H:%M')}")
        start_timestamp = self.prescription['taking_start_timestamp']
        start_timestamp: pd.Timestamp
        self.label_start_date.setText(f"복용시작일: {start_timestamp.strftime('%Y-%m-%d')}")
        self.label_medi_amount.setText(f"복용량: {self.prescription['eat_amount']} tab")
        self.label_day_duration.setText(f"복용기간: {self.prescription['day_duration']}일")
        self.label_daily_count.setText(f"하루복용횟수: {self.prescription['daily_eat_count']}회")
        try:
            medication_id = int(self.medication["medication_id"][0])
            image_bytes = self.controller.db_conn.find_image_by_medication_id_as_byte_stream(medication_id)
            byte_array = QByteArray(image_bytes.getvalue())
            medi_pixmap = QPixmap()
            medi_pixmap.loadFromData(byte_array)
            self.label_medi_image.setPixmap(medi_pixmap)
        except:
            traceback.print_exc()
            print(f"이미지 못찾음 medication id: {medication_id}, 이름: {self.medication['dl_name']}")

        self.btn_edit.clicked.connect(lambda state: self.create_form_taking_schedule())
        self.btn_detail.clicked.connect(lambda state: self.create_form_checking_schedule())

    def create_form_taking_schedule(self):
        self.form_taking = FormTakingSchedule(self.controller, self.medication, self.prescription)
        self.form_taking.exec_()

    def create_form_checking_schedule(self):
        try:
            self.form_checking = FormCheckingSchedule(self.controller, self.medication, self.prescription)
            self.form_checking.exec_()
        except:
            QMessageBox.about(self, '확인', "먼저 계획을 저장해주세요.")
            traceback.print_exc()

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        print("클릭된 정보", self.prescription, self.medication)
