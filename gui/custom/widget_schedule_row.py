
from PyQt5 import QtWidgets

from gui.compiled.compiled_widget_schedule_row import Ui_Widget_Schedule_Row


class ScheduleRow(QtWidgets.QWidget, Ui_Widget_Schedule_Row):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
