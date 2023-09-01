# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/checking_schedule.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_FormCheckingSchedule(object):
    def setupUi(self, FormCheckingSchedule):
        FormCheckingSchedule.setObjectName("FormCheckingSchedule")
        FormCheckingSchedule.resize(477, 672)
        FormCheckingSchedule.setStyleSheet("#FormCheckingSchedule{\n"
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
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(FormCheckingSchedule)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget = QtWidgets.QWidget(FormCheckingSchedule)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
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
        self.widget_lower = QtWidgets.QWidget(FormCheckingSchedule)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_lower.sizePolicy().hasHeightForWidth())
        self.widget_lower.setSizePolicy(sizePolicy)
        self.widget_lower.setObjectName("widget_lower")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_lower)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_lower)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 552))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_8.addWidget(self.scrollArea)
        self.widget_13 = QtWidgets.QWidget(self.widget_lower)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_8.addWidget(self.widget_13)
        self.widget_12 = QtWidgets.QWidget(self.widget_lower)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.btn_save = QtWidgets.QPushButton(self.widget_12)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_6.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(self.widget_12)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_6.addWidget(self.btn_cancel)
        self.verticalLayout_8.addWidget(self.widget_12)
        self.verticalLayout_9.addWidget(self.widget_lower)

        self.retranslateUi(FormCheckingSchedule)
        QtCore.QMetaObject.connectSlotsByName(FormCheckingSchedule)

    def retranslateUi(self, FormCheckingSchedule):
        _translate = QtCore.QCoreApplication.translate
        FormCheckingSchedule.setWindowTitle(_translate("FormCheckingSchedule", "Form"))
        self.label_medi_name.setText(_translate("FormCheckingSchedule", "타이레놀8시간이알서방정(아세트아미노펜)"))
        self.label.setText(_translate("FormCheckingSchedule", " 복용이력 관리"))
        self.btn_save.setText(_translate("FormCheckingSchedule", "투약이력 저장"))
        self.btn_cancel.setText(_translate("FormCheckingSchedule", "닫기"))
