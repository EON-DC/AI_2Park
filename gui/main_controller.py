from PyQt5 import QtCore, QtGui, QtWidgets
from gui.compiled.compiled_MainApp import Ui_MainApp
from database.db_connector import DBConnector


class UIController(QtWidgets.QWidget, Ui_MainApp):

    def __init__(self, db_conn: DBConnector):
        super().__init__()
        self.setupUi(self)
        self.db_conn = db_conn

    @staticmethod
    def show_error_message(message, traceback):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec_()
        traceback.print_exc()
