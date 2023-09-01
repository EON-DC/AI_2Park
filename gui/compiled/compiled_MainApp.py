# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/MainApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainApp(object):
    def setupUi(self, MainApp):
        MainApp.setObjectName("MainApp")
        MainApp.resize(1130, 800)
        MainApp.setStyleSheet("*{\n"
"    font: \"맑은 고딕\";\n"
"}\n"
"\n"
"#banner {\n"
"    background-color : #FFFFFF;\n"
"}\n"
"#banner BannerLabel{\n"
"    border-width: 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"#body{\n"
"    background-color : #F4F4F4;\n"
"}\n"
"\n"
"QStackedWidget {\n"
"    background-color : #ffffff;\n"
"}\n"
"\n"
"#widget_header{\n"
"    background-image: url(:/image/background_header.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left center;\n"
"    background-origin: content;\n"
"    border-width: 0px;\n"
"}\n"
"#label_section_title{\n"
"    font: 28pt \"배달의민족 주아\";\n"
"}\n"
"\n"
"#banner #widget_banner_head{\n"
"    background-color : #FFFFFF;\n"
"    border-bottom: 2px solid #D4D4D4;\n"
"}\n"
"\n"
"#banner QLabel{\n"
"    color: #7DB9C3;\n"
"}\n"
"\n"
"#banner #label_header{\n"
"    color: rgb(74, 134, 232);\n"
"    font: bold 12pt \"맑은 고딕\";\n"
"}\n"
"#label_user_info{\n"
"    color: rgb(74, 134, 232);\n"
"    font: bold 12pt \"맑은 고딕\";\n"
"    padding: 5px;\n"
"}\n"
"\n"
"#liner{\n"
"    background-color : #7DB9C3;\n"
"}\n"
"\n"
"#banner BannerButton {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #DFDFDF;\n"
"    border-radius: 20px;\n"
"}\n"
"#banner BannerButton:hover {\n"
"    background-color: #9FC5E8;\n"
"    border: 2px solid #C9DAF8;\n"
"}\n"
"#banner BannerButton:pressed {\n"
"    background-color: #4A86E8;\n"
"    border: 2px solid #86AEEF;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(MainApp)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_base = QtWidgets.QWidget(MainApp)
        self.widget_base.setObjectName("widget_base")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_base)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.body = QtWidgets.QWidget(self.widget_base)
        self.body.setObjectName("body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_header = QtWidgets.QWidget(self.body)
        self.widget_header.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_header.setObjectName("widget_header")
        self.label_section_title = QtWidgets.QLabel(self.widget_header)
        self.label_section_title.setGeometry(QtCore.QRect(250, 10, 570, 70))
        self.label_section_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_section_title.setObjectName("label_section_title")
        self.verticalLayout.addWidget(self.widget_header)
        self.stackedWidget = QtWidgets.QStackedWidget(self.body)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.layout_page_0 = QtWidgets.QVBoxLayout()
        self.layout_page_0.setSpacing(0)
        self.layout_page_0.setObjectName("layout_page_0")
        self.horizontalLayout_7.addLayout(self.layout_page_0)
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout_page_1 = QtWidgets.QVBoxLayout()
        self.layout_page_1.setSpacing(0)
        self.layout_page_1.setObjectName("layout_page_1")
        self.verticalLayout_4.addLayout(self.layout_page_1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.layout_page_2 = QtWidgets.QVBoxLayout()
        self.layout_page_2.setSpacing(0)
        self.layout_page_2.setObjectName("layout_page_2")
        self.verticalLayout_7.addLayout(self.layout_page_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.layout_page_3 = QtWidgets.QVBoxLayout()
        self.layout_page_3.setObjectName("layout_page_3")
        self.verticalLayout_8.addLayout(self.layout_page_3)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.layout_page_4 = QtWidgets.QVBoxLayout()
        self.layout_page_4.setSpacing(0)
        self.layout_page_4.setObjectName("layout_page_4")
        self.verticalLayout_9.addLayout(self.layout_page_4)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layout_page_5 = QtWidgets.QVBoxLayout()
        self.layout_page_5.setSpacing(0)
        self.layout_page_5.setObjectName("layout_page_5")
        self.horizontalLayout_5.addLayout(self.layout_page_5)
        self.stackedWidget.addWidget(self.page_5)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.body)
        self.banner = QtWidgets.QWidget(self.widget_base)
        self.banner.setMinimumSize(QtCore.QSize(150, 0))
        self.banner.setMaximumSize(QtCore.QSize(150, 16777215))
        self.banner.setObjectName("banner")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.banner)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.banner)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 70))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(72, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_locker = BannerLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_locker.sizePolicy().hasHeightForWidth())
        self.label_locker.setSizePolicy(sizePolicy)
        self.label_locker.setMinimumSize(QtCore.QSize(70, 70))
        self.label_locker.setMaximumSize(QtCore.QSize(70, 70))
        self.label_locker.setText("")
        self.label_locker.setScaledContents(True)
        self.label_locker.setObjectName("label_locker")
        self.verticalLayout_3.addWidget(self.label_locker)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.label_user_info = QtWidgets.QLabel(self.widget)
        self.label_user_info.setScaledContents(False)
        self.label_user_info.setWordWrap(True)
        self.label_user_info.setObjectName("label_user_info")
        self.verticalLayout_2.addWidget(self.label_user_info)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.widget_banner_3 = QtWidgets.QWidget(self.widget)
        self.widget_banner_3.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_banner_3.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_banner_3.setObjectName("widget_banner_3")
        self.btn_banner_3 = BannerButton(self.widget_banner_3)
        self.btn_banner_3.setGeometry(QtCore.QRect(100, 10, 160, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_banner_3.setIcon(icon)
        self.btn_banner_3.setIconSize(QtCore.QSize(60, 60))
        self.btn_banner_3.setObjectName("btn_banner_3")
        self.verticalLayout_2.addWidget(self.widget_banner_3)
        self.widget_banner_1 = QtWidgets.QWidget(self.widget)
        self.widget_banner_1.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_banner_1.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_banner_1.setObjectName("widget_banner_1")
        self.btn_banner_1 = BannerButton(self.widget_banner_1)
        self.btn_banner_1.setGeometry(QtCore.QRect(100, 10, 160, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/camera.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_banner_1.setIcon(icon1)
        self.btn_banner_1.setIconSize(QtCore.QSize(55, 55))
        self.btn_banner_1.setObjectName("btn_banner_1")
        self.verticalLayout_2.addWidget(self.widget_banner_1)
        self.widget_banner_4 = QtWidgets.QWidget(self.widget)
        self.widget_banner_4.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_banner_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_banner_4.setObjectName("widget_banner_4")
        self.btn_banner_4 = BannerButton(self.widget_banner_4)
        self.btn_banner_4.setGeometry(QtCore.QRect(100, 10, 160, 60))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/list-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_banner_4.setIcon(icon2)
        self.btn_banner_4.setIconSize(QtCore.QSize(60, 60))
        self.btn_banner_4.setObjectName("btn_banner_4")
        self.verticalLayout_2.addWidget(self.widget_banner_4)
        self.widget_banner_2 = QtWidgets.QWidget(self.widget)
        self.widget_banner_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_banner_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_banner_2.setObjectName("widget_banner_2")
        self.btn_banner_2 = BannerButton(self.widget_banner_2)
        self.btn_banner_2.setGeometry(QtCore.QRect(100, 10, 160, 60))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_banner_2.setIcon(icon3)
        self.btn_banner_2.setIconSize(QtCore.QSize(50, 50))
        self.btn_banner_2.setObjectName("btn_banner_2")
        self.verticalLayout_2.addWidget(self.widget_banner_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.banner)
        self.horizontalLayout.addWidget(self.widget_base)

        self.retranslateUi(MainApp)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainApp)

    def retranslateUi(self, MainApp):
        _translate = QtCore.QCoreApplication.translate
        MainApp.setWindowTitle(_translate("MainApp", "WD"))
        self.label_section_title.setText(_translate("MainApp", "TextLabel"))
        self.label_user_info.setText(_translate("MainApp", "TextLabel"))
        self.btn_banner_3.setText(_translate("MainApp", "홈화면으로   "))
        self.btn_banner_1.setText(_translate("MainApp", "실시간 분류     "))
        self.btn_banner_4.setText(_translate("MainApp", "경구약 확인       "))
        self.btn_banner_2.setText(_translate("MainApp", "저장 목록         "))
from gui.custom.bannerbutton import BannerButton
from gui.custom.bannerlabel import BannerLabel
