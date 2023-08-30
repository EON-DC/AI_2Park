# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/saved_prescription_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Saved_Prescription_Item(object):
    def setupUi(self, Saved_Prescription_Item):
        Saved_Prescription_Item.setObjectName("Saved_Prescription_Item")
        Saved_Prescription_Item.resize(806, 128)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Saved_Prescription_Item.sizePolicy().hasHeightForWidth())
        Saved_Prescription_Item.setSizePolicy(sizePolicy)
        Saved_Prescription_Item.setMinimumSize(QtCore.QSize(0, 0))
        Saved_Prescription_Item.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Saved_Prescription_Item.setStyleSheet("*{\n"
"    font: \"맑은 고딕\";\n"
"}\n"
"\n"
"#label_medi_name{\n"
"    font: bold 12pt;\n"
"}\n"
"\n"
"#btn_detail{\n"
"    font: 10pt;\n"
"}\n"
"\n"
"#label_saved_time{\n"
"    font: 10pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #9FC5E8;\n"
"    border: 2px solid #C9DAF8;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #4A86E8;\n"
"    border: 2px solid #86AEEF;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Saved_Prescription_Item)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Saved_Prescription_Item)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_medi_image = QtWidgets.QLabel(self.widget_2)
        self.label_medi_image.setMinimumSize(QtCore.QSize(0, 0))
        self.label_medi_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_medi_image.setText("")
        self.label_medi_image.setPixmap(QtGui.QPixmap(":/image/pill_sample_2.png"))
        self.label_medi_image.setScaledContents(True)
        self.label_medi_image.setObjectName("label_medi_image")
        self.verticalLayout_2.addWidget(self.label_medi_image)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(800, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget1 = QtWidgets.QWidget(self.widget_3)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_medi_name = QtWidgets.QLabel(self.widget1)
        self.label_medi_name.setObjectName("label_medi_name")
        self.horizontalLayout_2.addWidget(self.label_medi_name)
        self.label_saved_time = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_saved_time.sizePolicy().hasHeightForWidth())
        self.label_saved_time.setSizePolicy(sizePolicy)
        self.label_saved_time.setWordWrap(True)
        self.label_saved_time.setObjectName("label_saved_time")
        self.horizontalLayout_2.addWidget(self.label_saved_time)
        spacerItem = QtWidgets.QSpacerItem(231, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_edit = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy)
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout_2.addWidget(self.btn_edit)
        self.btn_detail = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_detail.sizePolicy().hasHeightForWidth())
        self.btn_detail.setSizePolicy(sizePolicy)
        self.btn_detail.setObjectName("btn_detail")
        self.horizontalLayout_2.addWidget(self.btn_detail)
        self.verticalLayout.addWidget(self.widget1)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_start_date = QtWidgets.QLabel(self.widget_4)
        self.label_start_date.setWordWrap(True)
        self.label_start_date.setObjectName("label_start_date")
        self.horizontalLayout_4.addWidget(self.label_start_date)
        self.label_day_duration = QtWidgets.QLabel(self.widget_4)
        self.label_day_duration.setObjectName("label_day_duration")
        self.horizontalLayout_4.addWidget(self.label_day_duration)
        self.label_medi_amount = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_medi_amount.sizePolicy().hasHeightForWidth())
        self.label_medi_amount.setSizePolicy(sizePolicy)
        self.label_medi_amount.setObjectName("label_medi_amount")
        self.horizontalLayout_4.addWidget(self.label_medi_amount)
        self.label_daily_count = QtWidgets.QLabel(self.widget_4)
        self.label_daily_count.setObjectName("label_daily_count")
        self.horizontalLayout_4.addWidget(self.label_daily_count)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Saved_Prescription_Item)
        QtCore.QMetaObject.connectSlotsByName(Saved_Prescription_Item)

    def retranslateUi(self, Saved_Prescription_Item):
        _translate = QtCore.QCoreApplication.translate
        Saved_Prescription_Item.setWindowTitle(_translate("Saved_Prescription_Item", "Form"))
        self.label_medi_name.setText(_translate("Saved_Prescription_Item", "팍스로비드정"))
        self.label_saved_time.setText(_translate("Saved_Prescription_Item", "저장일시: 2023-08-26 13:11"))
        self.btn_edit.setText(_translate("Saved_Prescription_Item", "정보\n"
"수정하기"))
        self.btn_detail.setText(_translate("Saved_Prescription_Item", "복용이력\n"
"관리"))
        self.label_start_date.setText(_translate("Saved_Prescription_Item", "복용시작일:2023-08-30"))
        self.label_day_duration.setText(_translate("Saved_Prescription_Item", "복용기간: 2일"))
        self.label_medi_amount.setText(_translate("Saved_Prescription_Item", "복용량:2 tab"))
        self.label_daily_count.setText(_translate("Saved_Prescription_Item", "하루복용횟수: 3회"))
from gui.compiled import my_qrc_rc
