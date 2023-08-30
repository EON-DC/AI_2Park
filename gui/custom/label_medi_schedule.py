from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ScheduleLabel(QtWidgets.QLabel):
    style = """
        QLabel{
            border: 1px solid #66BBBB;
        }
    """

    def __init__(self, taking_index, taking_time: tuple[int, int, int, int, int] = (0, 0, 0, 0, 0), parent=None, row=-1,
                 col=-1):
        super().__init__(parent=parent)
        self.setMinimumWidth(120)
        if taking_index == -1:
            return
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(self.style)
        self.taking_index = taking_index
        self.year, self.month, self.day, self.hour, self.minute = taking_time
        self.row_index = row
        self.col_index = col
        if self.hour < 12:
            self.converted_hour = self.hour
            self.label_text = f"{self.taking_index}회차 오전 {self.converted_hour:02d}:{self.minute:02d}"
        else:
            self.converted_hour = self.hour - 12
            self.label_text = f"{self.taking_index}회차 오후 {self.converted_hour:02d}:{self.minute:02d}"
        self.setText(self.label_text)

    def __repr__(self):
        return f"{self.taking_index} : {self.hour}:{self.minute}"

    def time_change(self, col, taking_time: tuple[int, int]):
        if col == self.col_index:
            self.hour, self.minute = taking_time
            if self.hour < 12:
                self.converted_hour = self.hour
                self.label_text = f"{self.taking_index}회차 오전 {self.converted_hour:02d}:{self.minute:02d}"
            else:
                self.converted_hour = self.hour - 12
                self.label_text = f"{self.taking_index}회차 오후 {self.converted_hour:02d}:{self.minute:02d}"
            self.setText(self.label_text)

    def get_schedule(self):
        return self.taking_index, self.year, self.month, self.day, self.hour, self.minute
