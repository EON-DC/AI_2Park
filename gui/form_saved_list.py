import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

from gui.compiled.compiled_Form_Saved_Medi_List import Ui_Form_Saved_Medi_List
from gui.custom.saved_prescription_item import SavedPrescriptionItem


class FormSavedList(QtWidgets.QWidget, Ui_Form_Saved_Medi_List):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()

    def set_up_initial(self):
        self.btn_new.clicked.connect(lambda state: self.create_new_medication_list())
        self.btn_delete.clicked.connect(lambda state: self.delete_selected_medi())

    def refresh_list_widget(self):
        self.listWidget.clear()
        # db에서 로그인 데이터 바탕으로 처방 정보 리스트 불러오기
        prescription_df = self.controller.db_conn.find_all_prescriptions_by_user_id(self.controller.user_df["user_id"][0])
        prescription_df:pd.DataFrame
        # 약 정보 가져오기
        temp_medi_df = pd.DataFrame()

        for idx, prescription in prescription_df.iterrows():
            item = QListWidgetItem(self.listWidget)
            medi_df = self.controller.db_conn.find_medication_by_medication_id(prescription["medication_id"])
            widget = SavedPrescriptionItem(self, self.controller, prescription, medi_df)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def create_new_medication_list(self):
        self.controller.selected_saved_list_id = None
        self.controller.set_page("camera")


    def delete_selected_medi(self):
        reply = QMessageBox.question(self, '확인', '해당 처방기록을 삭제하시겠습니까? 다시 불러올 수 없습니다.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        index_to_delete = self.listWidget.currentIndex().row()
        selected_item = self.listWidget.item(index_to_delete)
        selected_widget = self.listWidget.itemWidget(selected_item)
        selected_widget: SavedPrescriptionItem
        prescription_id = selected_widget.prescription["prescription_id"]
        if selected_widget is not None:
            selected_widget.deleteLater()
        self.listWidget.takeItem(index_to_delete)

        # todo : db 에서도 해당 약물 삭제하기
        self.controller.db_conn.delete_prescription_by_prescription_id(prescription_id)
