import sys
from multiprocessing import Process

import pandas as pd
from PyQt5 import QtWidgets

import gui.custom.form_loader

if __name__ == '__main__':
    ## 각 컬럼 width 최대로
    pd.set_option('display.max_colwidth', 150)
    ## rows 500
    pd.set_option('display.max_rows', 500)
    ## columns
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    process = Process(target=gui.custom.form_loader.run_loading_widget, args=(sys.argv, ))
    process.start()

    app = QtWidgets.QApplication(sys.argv)
    from gui.main_controller import UIController
    from database.db_connector import DBConnector
    # form_loader.show()
    # DB커넥터 개체 생성
    db_conn = DBConnector()

    # DB커넥터 DI 및 UI Controller 개체 생성
    controller = UIController(db_conn)
    process.kill()
    controller.show()

    # 에러메시지 출력
    sys.excepthook = lambda exctype, value, traceback: UIController.show_error_message(str(value), traceback)
    app.exec_()
