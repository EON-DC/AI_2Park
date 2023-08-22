import sys

from PyQt5 import QtWidgets

from gui.main_controller import UIController
from database.db_connector import DBConnector

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # DB커넥터 개체 생성
    db_conn = DBConnector()

    # DB커넥터 DI 및 UI Controller 개체 생성
    controller = UIController(db_conn)
    controller.show()

    # 에러메시지 출력
    sys.excepthook = lambda exctype, value, traceback: UIController.show_error_message(str(value), traceback)
    app.exec_()
