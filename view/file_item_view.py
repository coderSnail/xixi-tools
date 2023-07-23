from PyQt6.QtWidgets import QWidget

from ui.file_item_ui import Ui_file_item


class FileItemView(QWidget, Ui_file_item):
    def __init__(self, parent=None, file=None, data_configs=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.file = file
        self.data_configs = data_configs

        print(self.file, self.data_configs)
        self.label_file_name.setText(self.file)
        self.combo_file_type.addItems(self.data_configs)
