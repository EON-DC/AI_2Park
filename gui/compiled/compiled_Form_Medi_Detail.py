# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Form_Medi_Detail.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form_Medi_Detail(object):
    def setupUi(self, Form_Medi_Detail):
        Form_Medi_Detail.setObjectName("Form_Medi_Detail")
        Form_Medi_Detail.resize(970, 700)
        Form_Medi_Detail.setStyleSheet("*{\n"
"    font: \"맑은 고딕\";\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 10px;\n"
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
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Medi_Detail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form_Medi_Detail)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delete = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        self.btn_delete.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_delete.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_camera = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy)
        self.btn_camera.setMinimumSize(QtCore.QSize(100, 0))
        self.btn_camera.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_camera.setObjectName("btn_camera")
        self.horizontalLayout.addWidget(self.btn_camera)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(Form_Medi_Detail)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form_Medi_Detail)
        QtCore.QMetaObject.connectSlotsByName(Form_Medi_Detail)

    def retranslateUi(self, Form_Medi_Detail):
        _translate = QtCore.QCoreApplication.translate
        Form_Medi_Detail.setWindowTitle(_translate("Form_Medi_Detail", "Form"))
        self.btn_delete.setText(_translate("Form_Medi_Detail", "선택 삭제하기"))
        self.btn_camera.setText(_translate("Form_Medi_Detail", "다시 촬영하기"))
