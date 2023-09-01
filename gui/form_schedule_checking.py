import pickle

import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QMessageBox

from gui.compiled.compiled_checking_schedule import Ui_FormCheckingSchedule
from gui.custom.widget_checking_row import CheckingRow


class FormCheckingSchedule(QtWidgets.QDialog, Ui_FormCheckingSchedule):
    def __init__(self, main_controller, medication: pd.DataFrame, prescription: pd.Series):
        super().__init__()
        self.controller = main_controller
        self.medication = medication
        self.prescription = prescription
        self.plan_schedule = self.controller.db_conn.find_schedule_by_prescription_id(prescription["prescription_id"])
        self.predict_model = None
        self.setupUi(self)
        self.day_group = list()
        self.set_up_initial()

    def set_up_initial(self):
        self.btn_save.clicked.connect(lambda state: self.save_plan())
        self.btn_cancel.clicked.connect(lambda state: self.close())
        self.label_medi_name.setText(self.medication['dl_name'][0])
        with open('model/random_forest_model.pkl', 'rb') as model_file:  # 학습한 모델 불러오기
            self.predict_model = pickle.load(model_file)
        self.set_up_plan_schedule()

    def save_plan(self):
        reply = QMessageBox.question(self, '확인', '이대로 저장하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        for label in self.day_group:
            schedule_id, bool_value = label.get_state()
            self.controller.db_conn.update_schedule_by_schedule_id(schedule_id, bool_value)
        QMessageBox.about(self, "결과", f"{len(self.day_group)}개의 복용 상태를 저장하였습니다.")
        self.close()

    # 데이터 베이스 수행 여부 저장
    def set_up_plan_schedule(self):
        self.plan_schedule: pd.DataFrame
        # 칼럼 생성
        widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        h_layout = QHBoxLayout(widget)
        widget.setLayout(h_layout)
        label_spacer = QLabel("                ", parent=widget)
        label_index = QLabel(f"복용 회차  ", parent=widget)
        label_datetime = QLabel(f"복용 시간  ", parent=widget)
        label_checkbox = QLabel(f"복용 확률  ", parent=widget)
        label_predict_value = QLabel(f"        복용 여부 체크 ", parent=widget)
        h_layout.addWidget(label_spacer)
        h_layout.addWidget(label_index)
        h_layout.addWidget(label_datetime)
        h_layout.addWidget(label_checkbox)
        h_layout.addWidget(label_predict_value)
        self.verticalLayout.addWidget(widget)

        daily_eat_count = self.prescription["daily_eat_count"]
        # 예측 확률
        taking_index_list = np.arange(1, 57).reshape((-1, 1))
        predic_result = self.predict_model.predict_proba(taking_index_list)
        plan_group = list()
        buffer_date = None
        # 불러온 저장 위젯 생성
        for idx, (_, plan), in enumerate(self.plan_schedule.iterrows()):
            if buffer_date is not None and buffer_date != plan['plan_timestamp'].strftime('%Y-%m-%d'):
                row = CheckingRow(plan_group, self)
                self.verticalLayout.addWidget(row)
                plan_group = list()
            buffer_date = plan['plan_timestamp'].strftime('%Y-%m-%d')
            plan_group.append((plan, predic_result[idx]))
        if len(plan_group) != 0:  # 잔여 기록 추가
            row = CheckingRow(plan_group, self)
            self.verticalLayout.addWidget(row)
