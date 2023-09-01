# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/taking_scheduler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormTakingScheduler(object):
    def setupUi(self, FormTakingScheduler):
        FormTakingScheduler.setObjectName("FormTakingScheduler")
        FormTakingScheduler.resize(776, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormTakingScheduler.sizePolicy().hasHeightForWidth())
        FormTakingScheduler.setSizePolicy(sizePolicy)
        FormTakingScheduler.setStyleSheet("#FormTakingScheduler{\n"
"    background-color: white;\n"
"}\n"
"\n"
"*{\n"
"    font: \"맑은 고딕\";\n"
"}\n"
"\n"
"#label_medi_name{\n"
"    font: bold 12pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #9FC5E8;\n"
"    border: 2px solid #C9DAF8;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4A86E8;\n"
"    border: 2px solid #86AEEF;\n"
"}\n"
"#widget_lower, #widget_upper {\n"
"    border: 2px solid #BABCBC;\n"
"}")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(FormTakingScheduler)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(FormTakingScheduler)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(222, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_medi_name = QtWidgets.QLabel(self.widget)
        self.label_medi_name.setObjectName("label_medi_name")
        self.horizontalLayout_2.addWidget(self.label_medi_name)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(222, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_9.addWidget(self.widget)
        self.widget_upper = QtWidgets.QWidget(FormTakingScheduler)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_upper.sizePolicy().hasHeightForWidth())
        self.widget_upper.setSizePolicy(sizePolicy)
        self.widget_upper.setObjectName("widget_upper")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_upper)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_5 = QtWidgets.QWidget(self.widget_upper)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setMinimumSize(QtCore.QSize(250, 0))
        self.widget_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_medi_image = QtWidgets.QLabel(self.widget_5)
        self.label_medi_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_medi_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_medi_image.setText("")
        self.label_medi_image.setPixmap(QtGui.QPixmap(":/image/pill_sample_3.png"))
        self.label_medi_image.setScaledContents(True)
        self.label_medi_image.setObjectName("label_medi_image")
        self.verticalLayout_2.addWidget(self.label_medi_image)
        self.horizontalLayout_7.addWidget(self.widget_5)
        self.widget_4 = QtWidgets.QWidget(self.widget_upper)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_start = QtWidgets.QDateEdit(self.widget_2)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.horizontalLayout.addWidget(self.dateEdit_start)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_day_duration = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox_day_duration.setMinimum(1)
        self.spinBox_day_duration.setMaximum(14)
        self.spinBox_day_duration.setObjectName("spinBox_day_duration")
        self.horizontalLayout.addWidget(self.spinBox_day_duration)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_taking_amount = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.spinBox_taking_amount.setDecimals(1)
        self.spinBox_taking_amount.setMinimum(1.0)
        self.spinBox_taking_amount.setMaximum(5.0)
        self.spinBox_taking_amount.setSingleStep(0.5)
        self.spinBox_taking_amount.setObjectName("spinBox_taking_amount")
        self.horizontalLayout.addWidget(self.spinBox_taking_amount)
        self.label_24 = QtWidgets.QLabel(self.widget_2)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout.addWidget(self.label_24)
        self.spinBox_daily_eat_count = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox_daily_eat_count.setMinimum(1)
        self.spinBox_daily_eat_count.setMaximum(4)
        self.spinBox_daily_eat_count.setObjectName("spinBox_daily_eat_count")
        self.horizontalLayout.addWidget(self.spinBox_daily_eat_count)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.spinBox_first_offset = QtWidgets.QSpinBox(self.widget_3)
        self.spinBox_first_offset.setMinimum(1)
        self.spinBox_first_offset.setMaximum(1)
        self.spinBox_first_offset.setObjectName("spinBox_first_offset")
        self.horizontalLayout_3.addWidget(self.spinBox_first_offset)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_taking_count = QtWidgets.QLabel(self.widget_3)
        self.label_taking_count.setObjectName("label_taking_count")
        self.horizontalLayout_3.addWidget(self.label_taking_count)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_create_table = QtWidgets.QPushButton(self.widget_3)
        self.btn_create_table.setObjectName("btn_create_table")
        self.horizontalLayout_3.addWidget(self.btn_create_table)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout_7.addWidget(self.widget_4)
        self.verticalLayout_9.addWidget(self.widget_upper)
        self.widget_lower = QtWidgets.QWidget(FormTakingScheduler)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_lower.sizePolicy().hasHeightForWidth())
        self.widget_lower.setSizePolicy(sizePolicy)
        self.widget_lower.setObjectName("widget_lower")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_lower)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_lower_columns = QtWidgets.QWidget(self.widget_lower)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_lower_columns.sizePolicy().hasHeightForWidth())
        self.widget_lower_columns.setSizePolicy(sizePolicy)
        self.widget_lower_columns.setObjectName("widget_lower_columns")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_lower_columns)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.widget_10 = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.label_8 = QtWidgets.QLabel(self.widget_10)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout_5.addWidget(self.widget_10)
        self.widget_time_edit = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_time_edit.setObjectName("widget_time_edit")
        self.horizontalLayout_5.addWidget(self.widget_time_edit)
        self.widget_taking_first = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_taking_first.setObjectName("widget_taking_first")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_taking_first)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.widget_taking_first)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.timeEdit = QtWidgets.QTimeEdit(self.widget_taking_first)
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 8, 29), QtCore.QTime(9, 0, 0)))
        self.timeEdit.setDate(QtCore.QDate(2023, 8, 29))
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_3.addWidget(self.timeEdit)
        self.horizontalLayout_5.addWidget(self.widget_taking_first)
        self.widget_taking_second = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_taking_second.setObjectName("widget_taking_second")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_taking_second)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.widget_taking_second)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.widget_taking_second)
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 8, 29), QtCore.QTime(13, 0, 0)))
        self.timeEdit_2.setDate(QtCore.QDate(2023, 8, 29))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.verticalLayout_4.addWidget(self.timeEdit_2)
        self.horizontalLayout_5.addWidget(self.widget_taking_second)
        self.widget_taking_third = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_taking_third.setObjectName("widget_taking_third")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_taking_third)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.widget_taking_third)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.widget_taking_third)
        self.timeEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 8, 29), QtCore.QTime(18, 0, 0)))
        self.timeEdit_3.setDate(QtCore.QDate(2023, 8, 29))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.verticalLayout_5.addWidget(self.timeEdit_3)
        self.horizontalLayout_5.addWidget(self.widget_taking_third)
        self.widget_taking_fourth = QtWidgets.QWidget(self.widget_lower_columns)
        self.widget_taking_fourth.setObjectName("widget_taking_fourth")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_taking_fourth)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.widget_taking_fourth)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.widget_taking_fourth)
        self.timeEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 8, 29), QtCore.QTime(21, 0, 0)))
        self.timeEdit_4.setDate(QtCore.QDate(2023, 8, 29))
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.verticalLayout_6.addWidget(self.timeEdit_4)
        self.horizontalLayout_5.addWidget(self.widget_taking_fourth)
        spacerItem5 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_8.addWidget(self.widget_lower_columns)
        self.widget_table = QtWidgets.QWidget(self.widget_lower)
        self.widget_table.setObjectName("widget_table")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_table)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame = QtWidgets.QFrame(self.widget_table)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_4.addWidget(self.label_20)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_4.addWidget(self.label_16)
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_4.addWidget(self.label_21)
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_4.addWidget(self.label_17)
        spacerItem8 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout_10.addWidget(self.frame)
        self.verticalLayout_8.addWidget(self.widget_table)
        self.widget_12 = QtWidgets.QWidget(self.widget_lower)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.btn_save = QtWidgets.QPushButton(self.widget_12)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_6.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.widget_12)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_6.addWidget(self.btn_cancel)
        self.verticalLayout_8.addWidget(self.widget_12)
        self.verticalLayout_9.addWidget(self.widget_lower)

        self.retranslateUi(FormTakingScheduler)
        QtCore.QMetaObject.connectSlotsByName(FormTakingScheduler)

    def retranslateUi(self, FormTakingScheduler):
        _translate = QtCore.QCoreApplication.translate
        FormTakingScheduler.setWindowTitle(_translate("FormTakingScheduler", "Form"))
        self.label_medi_name.setText(_translate("FormTakingScheduler", "타이레놀8시간이알서방정(아세트아미노펜)"))
        self.label.setText(_translate("FormTakingScheduler", " 복용스케줄 작성"))
        self.label_2.setText(_translate("FormTakingScheduler", "부터"))
        self.label_3.setText(_translate("FormTakingScheduler", "일 동안 하루에"))
        self.label_24.setText(_translate("FormTakingScheduler", "알씩"))
        self.label_4.setText(_translate("FormTakingScheduler", "회 복용한다."))
        self.label_5.setText(_translate("FormTakingScheduler", "복용 시작 첫날에는"))
        self.label_6.setText(_translate("FormTakingScheduler", "회 복용한다."))
        self.label_taking_count.setText(_translate("FormTakingScheduler", "총 1회차 복용"))
        self.btn_create_table.setText(_translate("FormTakingScheduler", "계획표 생성"))
        self.label_8.setText(_translate("FormTakingScheduler", "복용일자"))
        self.label_9.setText(_translate("FormTakingScheduler", "첫번째 약"))
        self.label_10.setText(_translate("FormTakingScheduler", "두번째 약"))
        self.label_11.setText(_translate("FormTakingScheduler", "세번째 약"))
        self.label_12.setText(_translate("FormTakingScheduler", "네번째 약"))
        self.label_13.setText(_translate("FormTakingScheduler", "2023-08-27"))
        self.label_7.setText(_translate("FormTakingScheduler", "1회차"))
        self.label_14.setText(_translate("FormTakingScheduler", "오전 09:00"))
        self.label_19.setText(_translate("FormTakingScheduler", "2회차"))
        self.label_15.setText(_translate("FormTakingScheduler", "오후 01:00"))
        self.label_20.setText(_translate("FormTakingScheduler", "3회차"))
        self.label_16.setText(_translate("FormTakingScheduler", "오후 6:00"))
        self.label_21.setText(_translate("FormTakingScheduler", "4회차"))
        self.label_17.setText(_translate("FormTakingScheduler", "오후 9:00"))
        self.btn_save.setText(_translate("FormTakingScheduler", "계획 저장"))
        self.btn_cancel.setText(_translate("FormTakingScheduler", "취소"))
