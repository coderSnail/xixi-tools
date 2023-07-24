from PyQt6.QtWidgets import QWidget

from ui.file_item_ui import Ui_file_item


class FileItemView(QWidget, Ui_file_item):
    def __init__(self, parent=None, file=None, data_config=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.file = file
        self.data_config = data_config

        self.label_file_name.setText(self.file)
        # 设置文件类型下拉框
        self.combo_file_type.addItems(list(self.data_config.keys()))
        # 自动识别文件类型
        for key in self.data_config.keys():
            if file.upper().__contains__(self.data_config[key]['channel_id'].upper()) and file.upper().__contains__(self.data_config[key]['type_id'].upper()):
                self.combo_file_type.setCurrentText(key)
