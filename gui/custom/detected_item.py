import pandas as pd
from PyQt5 import QtGui, QtWidgets

from gui.compiled.compiled_detected_medi_item import Ui_Widget_Detected_Item


class DetectedItem(QtWidgets.QWidget, Ui_Widget_Detected_Item):
    def __init__(self, parent=None, controller=None, medication=None):
        super().__init__(parent)
        self.setupUi(self)
        self.form_camera = parent
        self.controller = controller
        self.medication = medication
        self.set_up_initial()

    def set_up_initial(self):
        self.btn_delete.clicked.connect(self.close)
        self.btn_save.clicked.connect(lambda state: self.add_medication_to_controller())
        self.label_medi_name.setText(self.medication["dl_name"][0])

    def activate_item(self):
        self.btn_delete.clicked.connect(lambda state: self.close())

    def deleteLater(self) -> None:
        self.form_camera.predicted_medication_mapping_list.remove(self.get_medi_code())
        self.form_camera.refresh_medication_count()
        super().deleteLater()

    def get_medi_code(self):
        return int(self.medication["dl_mapping_code"][0][2:])

    def add_medication_to_controller(self):
        self.btn_save.setEnabled(False)
        # todo : controller로 해당 로직 옮겨야함
        user_id = self.controller.user_df['user_id'][0]
        mapping_code = int(self.medication['dl_mapping_code'][0][2:]) # 기본적으로 붙은 "K-"지워줘야함
        created_prescription_df = self.controller.db_conn.create_prescription_with_medication_mapping_id(
            user_id,
            mapping_code,
            1,  # day_duration
            1,  # eat_amount
            1,  # daily_eat_count
        )

        self.controller.selected_prescription_df = pd.concat(
            [self.controller.selected_prescription_df, created_prescription_df])
