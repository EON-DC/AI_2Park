import traceback

import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDateTime, QTime, QByteArray
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QTimeEdit, QMessageBox

from gui.compiled.compiled_taking_scheduler import Ui_FormTakingScheduler
from gui.custom.label_medi_schedule import ScheduleLabel


class FormTakingSchedule(QtWidgets.QDialog, Ui_FormTakingScheduler):
    def __init__(self, main_controller, medication, prescription: pd.Series):
        super().__init__()
        self.controller = main_controller
        self.medication = medication
        self.prescription = prescription  # series
        self.setupUi(self)
        self.saved_schedule_list = list()
        self.set_up_initial()

    def set_up_initial(self):
        # prescription 정보대로 수정하기
        now_qtime = QDateTime.currentDateTime()
        self.dateEdit_start.setDate(now_qtime.date())
        self.label_medi_name.setText(self.medication['dl_name'][0])
        try:
            self.spinBox_day_duration.stepBy(self.prescription["day_duration"] - 1)
            self.spinBox_taking_amount.stepBy(int((self.prescription["eat_amount"] / 0.5) - 2))
            self.spinBox_daily_eat_count.stepBy(self.prescription["daily_eat_count"] - 1)
        except Exception:
            traceback.print_exc()
        # time edit 삭제

        self.widget_taking_first.setVisible(False)
        self.widget_taking_second.setVisible(False)
        self.widget_taking_third.setVisible(False)
        self.widget_taking_fourth.setVisible(False)

        self.widget_time_edit.setLayout(QHBoxLayout(self.widget_lower_columns))

        # 이미지 조회
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

        # 스핀박스 조절할 때마다 계산하도록
        self.spinBox_daily_eat_count.valueChanged.connect(lambda val: self.update_taking_count())
        self.spinBox_daily_eat_count.valueChanged.connect(lambda val: self.spinBox_first_offset.setMaximum(val))
        self.spinBox_day_duration.valueChanged.connect(lambda val: self.update_taking_count())
        self.spinBox_first_offset.valueChanged.connect(lambda val: self.create_schedule_table())
        # 아래 박스 안보이게
        # self.widget_lower.setVisible(False)
        self.create_schedule_table()

        # 계획표 생성 버튼 누르면 보이게
        self.btn_create_table.setVisible(False)
        # self.btn_create_table.clicked.connect(lambda state: self.create_schedule_table())

        # 계획표 저장 연결
        self.btn_save.clicked.connect(lambda state: self.save_schedule_as_label())
        self.btn_cancel.clicked.connect(lambda state: self.close())

    def update_taking_count(self):
        day_duration = int(self.spinBox_day_duration.text())
        daily_eat_count = int(self.spinBox_daily_eat_count.text())
        total_count = day_duration * daily_eat_count
        self.label_taking_count.setText(f"(총 {total_count}회차 복용)")
        self.create_schedule_table()

    def create_schedule_table(self):
        callable_day_count = ["첫번째", "두번째", "세번째", "네번째"]
        default_time_setting = [[9], (9, 21), (9, 13, 18), (9, 13, 17, 21)]

        self.saved_schedule_list.clear()
        self.widget_lower.setVisible(True)
        daily_taking_count = int(self.spinBox_daily_eat_count.text())
        day_duration = int(self.spinBox_day_duration.text())
        total_count = daily_taking_count * day_duration
        start_date = self.dateEdit_start.date()
        first_taking_count = int(self.spinBox_first_offset.text())
        time_edit_list = list()

        # 칼럼 비우기
        h_layout = self.widget_time_edit.layout()
        while h_layout.count():
            item = h_layout.takeAt(0)
            item.widget().deleteLater()

        # 로우 비우기
        v_table_layout = self.widget_table.layout()
        while v_table_layout.count():
            item = v_table_layout.takeAt(0)
            item.widget().deleteLater()

        # TimeEdit 칼럼 설정
        for idx in range(0, daily_taking_count):
            widget = QtWidgets.QWidget(self.widget_time_edit)
            widget.setMinimumWidth(120)
            h_layout.addWidget(widget)
            v_layout = QVBoxLayout(widget)
            widget.setLayout(v_layout)
            # 몇 번째 약인지 텍스트 저장
            label = QLabel(f"{callable_day_count[idx]} 약")
            label.setAlignment(Qt.AlignCenter)
            v_layout.addWidget(label)
            time_edit = QTimeEdit(widget)
            time_edit.timeChanged.connect(lambda q_time, col_index=idx: self.update_time_schedule(q_time, col_index))
            qtime = QTime(default_time_setting[daily_taking_count - 1][idx], 0, 0)
            time_edit.setTime(qtime)
            time_edit_list.append(qtime)
            v_layout.addWidget(time_edit)

        taking_index = 0

        offset = daily_taking_count - first_taking_count
        # row 설정
        if offset > 0:
            day_duration += 1
        for row in range(0, day_duration):
            widget = QtWidgets.QWidget(self.widget_table)
            h_table_layout = QHBoxLayout(widget)
            widget.setLayout(h_table_layout)

            left_spacer = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding,
                                                QtWidgets.QSizePolicy.Minimum)
            h_table_layout.addItem(left_spacer)

            year, month, day = start_date.addDays(row).getDate()
            date_label = QLabel(f"{year}-{month:02d}-{day:02d}", parent=widget)
            date_label.setStyleSheet("border: 1px solid #E8864A; padding: 5px;")
            date_label.setAlignment(Qt.AlignCenter)
            h_table_layout.addWidget(date_label)

            for col in range(0, daily_taking_count):
                offset -= 1
                if offset >= 0:
                    h_table_layout.addWidget(ScheduleLabel(-1, (0, 0), self))
                    continue
                if taking_index + 1 > total_count:
                    h_table_layout.addWidget(ScheduleLabel(-1, (0, 0), self))
                    continue
                hour = time_edit_list[col].hour()
                minute = time_edit_list[col].minute()
                taking_index += 1
                schedule_label = ScheduleLabel(taking_index, (year, month, day, hour, minute), self, row, col)
                h_table_layout.addWidget(schedule_label)
                self.saved_schedule_list.append(schedule_label)

            right_spacer = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding,
                                                 QtWidgets.QSizePolicy.Minimum)
            h_table_layout.addItem(right_spacer)

            v_table_layout.addWidget(widget)

    def update_time_schedule(self, q_time: QTime, col_index: int):
        hour = q_time.hour()
        min = q_time.minute()
        for lb in self.saved_schedule_list:
            lb.time_change(col_index, (hour, min))

    def save_schedule_as_label(self):
        prescription_id = self.prescription['prescription_id']
        day_duration = int(self.spinBox_day_duration.text())
        eat_amount = float(self.spinBox_taking_amount.text())
        daily_eat_count = int(self.spinBox_daily_eat_count.text())
        first_day_eat_count = int(self.spinBox_first_offset.text())
        taking_start_timestamp = self.dateEdit_start.date()
        self.controller.db_conn.update_prescription(prescription_id,
                                                    day_duration,
                                                    eat_amount,
                                                    daily_eat_count,
                                                    first_day_eat_count,
                                                    taking_start_timestamp)
        self.controller.db_conn.delete_schedule_by_prescription_id(prescription_id)
        for schedule in self.saved_schedule_list:
            schedule: ScheduleLabel
            taking_index = schedule.taking_index
            year = schedule.year
            month = schedule.month
            day = schedule.day
            hour = schedule.hour
            minute = schedule.minute
            self.controller.db_conn.create_schedule_by_prescription_id_and_taking_index_and_plan_timestamp(
                prescription_id, taking_index, year, month, day, hour, minute
            )
            print("DB등록됨 : ", schedule)
        QMessageBox.about(self, "알림", f"{len(self.saved_schedule_list)} 개의 계획이 저장됐습니다.")
        self.controller.form_detail.refresh_list_widget()
        self.controller.form_saved_list.refresh_list_widget()
        self.close()
