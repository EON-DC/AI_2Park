import numpy as np
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QCheckBox, QVBoxLayout

from gui.compiled.compiled_widget_checking_row import Ui_Widget_Checking_Row


class CheckLabel(QtWidgets.QWidget):
    hover_style = """        
            border : 1px solid #31599A;
            background-color: #86AEEF;
        """
    press_style = """
            border : 1px solid #31599A;
            background-color: #4A86E8;
    """
    default_style = """
        QLabel{
            border : 1px solid #31599A;
            background-color: #FFFFFF;
        }
    """

    def __init__(self, plan: pd.Series, predict_value: np.float64, parent):
        super().__init__(parent=parent)
        self.plan = plan
        self.predict_value = predict_value * 100
        self.h_layout = QHBoxLayout(self)
        self.setLayout(self.h_layout)
        self.label_text = QLabel(
            f"{plan['taking_index']}회차      {plan['plan_timestamp'].strftime('%H:%M')}       {self.predict_value[1]:2.1f}%",
            self)
        self.h_layout.addWidget(self.label_text)
        right_spacer = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
        self.h_layout.addItem(right_spacer)
        self.check_box = QCheckBox(self)
        self.h_layout.addWidget(self.check_box)

        if self.plan['has_taken'] is True:
            self.check_box.setChecked(True)
        else:
            self.check_box.setChecked(False)

        self.setStyleSheet(self.default_style)

    def get_state(self):
        return self.plan["schedule_id"], self.check_box.isChecked()

    def set_check(self, value: bool):
        self.check_box.setChecked(value)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        now_state = self.check_box.checkState()
        self.check_box.setChecked(not now_state)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.hover_style)

    def mousePressEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.press_style)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.default_style)


class WidgetDate(QtWidgets.QLabel):
    hover_style = """
        #widget_date{
            background: transparent;
        }"""
    press_style = """
        #widget_date{
            background-color: #E8864A;
        }
    """
    default_style = """
        #widget_date{
            border: 2px solid #64686B;
            background: transparent;
        }
    """

    def __init__(self, date_str, parent):
        super().__init__(date_str, parent=parent)
        self.setStyleSheet(self.default_style)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.hover_style)

    def mousePressEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.press_style)
        self.parent().mousePressEvent(a0)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.setStyleSheet(self.default_style)
        self.parent().mouseReleaseEvent(a0)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.default_style)


class CheckingRow(QtWidgets.QWidget, Ui_Widget_Checking_Row):
    hover_style = """
        #frame {
            background-color: #ffffff;
            border: 2px solid #E8864A;
        }
    """
    press_style = """
        #frame {
            background-color: #F7D6C2;
            border: 2px solid #E8864A
        }
    """
    default_style = """
        #frame {
            background-color: #ffffff;
            border: 2px solid #ffffff
        }
    """

    def __init__(self, plan_list: list[tuple[pd.Series, np.float64]], parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.plan_list = list()
        self.predict_list = list()
        self.setStyleSheet(self.default_style)
        for i in plan_list:
            series, predict_value = i
            self.plan_list.append(series)
            self.predict_list.append(predict_value)
        self.v_layout = self.widget_list.layout()
        self.row_list = list()

        self.layout_date = self.widget_date.layout()
        self.date_widget = WidgetDate(self.plan_list[0]['plan_timestamp'].strftime('%Y-%m-%d'), self)
        self.layout_date.addWidget(self.date_widget)
        self.set_up_initial()

    def set_up_initial(self):
        for idx, plan in enumerate(self.plan_list):
            label = CheckLabel(plan, self.predict_list[idx], self)
            self.row_list.append(label)
            self.parent().day_group.append(label)
            self.v_layout.addWidget(label)

    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None:
        now_state = self.row_list[0].check_box.checkState()
        for i in self.row_list:
            i.set_check(not now_state)

    def enterEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.hover_style)

    def mousePressEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.press_style)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.setStyleSheet(self.default_style)
