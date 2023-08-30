# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/detail_medication_item.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Detail_Item(object):
    def setupUi(self, Detail_Item):
        Detail_Item.setObjectName("Detail_Item")
        Detail_Item.resize(836, 132)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Detail_Item.sizePolicy().hasHeightForWidth())
        Detail_Item.setSizePolicy(sizePolicy)
        Detail_Item.setMinimumSize(QtCore.QSize(0, 0))
        Detail_Item.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Detail_Item.setStyleSheet("*{\n"
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Detail_Item)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Detail_Item)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(5)
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
        self.label_medi_image.setPixmap(QtGui.QPixmap(":/image/pill_sample_3.png"))
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_medi_name = QtWidgets.QLabel(self.widget1)
        self.label_medi_name.setObjectName("label_medi_name")
        self.horizontalLayout_2.addWidget(self.label_medi_name)
        spacerItem = QtWidgets.QSpacerItem(222, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_taking_schedule = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_taking_schedule.sizePolicy().hasHeightForWidth())
        self.btn_taking_schedule.setSizePolicy(sizePolicy)
        self.btn_taking_schedule.setObjectName("btn_taking_schedule")
        self.horizontalLayout_2.addWidget(self.btn_taking_schedule)
        self.btn_checking_schedule = QtWidgets.QPushButton(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_checking_schedule.sizePolicy().hasHeightForWidth())
        self.btn_checking_schedule.setSizePolicy(sizePolicy)
        self.btn_checking_schedule.setObjectName("btn_checking_schedule")
        self.horizontalLayout_2.addWidget(self.btn_checking_schedule)
        self.verticalLayout.addWidget(self.widget1)
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_1 = QtWidgets.QLabel(self.widget_4)
        self.label_1.setMinimumSize(QtCore.QSize(30, 0))
        self.label_1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_4.addWidget(self.label_1)
        self.label_class_no = QtWidgets.QLabel(self.widget_4)
        self.label_class_no.setObjectName("label_class_no")
        self.horizontalLayout_4.addWidget(self.label_class_no)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_etc_otc = QtWidgets.QLabel(self.widget_4)
        self.label_etc_otc.setObjectName("label_etc_otc")
        self.horizontalLayout_4.addWidget(self.label_etc_otc)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Detail_Item)
        QtCore.QMetaObject.connectSlotsByName(Detail_Item)

    def retranslateUi(self, Detail_Item):
        _translate = QtCore.QCoreApplication.translate
        Detail_Item.setWindowTitle(_translate("Detail_Item", "Form"))
        self.label_medi_name.setText(_translate("Detail_Item", "타이레놀8시간이알서방정(아세트아미노펜)"))
        self.btn_taking_schedule.setText(_translate("Detail_Item", "복용스케줄\n"
" 입력"))
        self.btn_checking_schedule.setText(_translate("Detail_Item", "복용이력\n"
"관리"))
        self.label_1.setText(_translate("Detail_Item", "효능:"))
        self.label_class_no.setText(_translate("Detail_Item", "[114] 해열·진통·소염제"))
        self.label_2.setText(_translate("Detail_Item", "분류:"))
        self.label_etc_otc.setText(_translate("Detail_Item", "일반의약품"))
from gui.compiled import my_qrc_rc
