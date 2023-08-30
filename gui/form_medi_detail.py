import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QMessageBox

from gui.compiled.compiled_Form_Medi_Detail import Ui_Form_Medi_Detail
from gui.custom.detail_medication_item import DetailMedicationItem


class FormMedicationDetails(QtWidgets.QWidget, Ui_Form_Medi_Detail):

    def __init__(self, main_controller):
        super().__init__()
        self.controller = main_controller
        self.setupUi(self)
        self.set_up_initial()
        self.btn_delete.clicked.connect(lambda state: self.delete_selected_medi())

    def set_up_initial(self):
        self.btn_camera.clicked.connect(lambda state: self.go_to_camera())

    def refresh_list_widget(self):
        self.listWidget.clear()
        prescription_df = self.controller.selected_prescription_df
        if len(prescription_df) == 0:
            self.listWidget.addItem(QListWidgetItem("확인된 약물이 없습니다."))
            return
        prescription_df: pd.DataFrame
        for idx, prescription in prescription_df.iterrows():
            item = QListWidgetItem(self.listWidget)
            medi_df = self.controller.db_conn.find_medication_by_medication_id(prescription["medication_id"])
            widget = DetailMedicationItem(self, self.controller, medi_df, prescription)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

    def go_to_camera(self):
        self.controller.set_page("camera")
        self.controller.form_camera.temp_medi_df = self.controller.selected_prescription_df.copy()

    def delete_selected_medi(self):
        reply = QMessageBox.question(self, '확인', '선택 경구약을 삭제하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return
        index_to_delete = self.listWidget.currentIndex().row()
        selected_item = self.listWidget.item(index_to_delete)
        selected_widget = self.listWidget.itemWidget(selected_item)
        selected_widget: DetailMedicationItem
        prescription_id = selected_widget.prescription["prescription_id"]
        if selected_widget is not None:
            selected_widget.deleteLater()
        self.listWidget.takeItem(index_to_delete)

        # todo : controller 에서도 해당 약물 삭제하기
        self.controller.selected_prescription_df = self.controller.selected_prescription_df[
            self.controller.selected_prescription_df["prescription_id"] != prescription_id]
        print(self.controller.selected_prescription_df)
        # todo : db 에서도 해당 약물 삭제하기
        self.controller.db_conn.delete_prescription_by_prescription_id(prescription_id)
