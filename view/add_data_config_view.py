from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget
from qfluentwidgets import InfoBar, InfoBarPosition

from ui.add_data_config_ui import Ui_data_config_widget
from util import common_util
from util.common_util import get_real_path


class AddDataConfigView(QWidget, Ui_data_config_widget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(get_real_path('resources', 'xixi.ico')))
        self.line_data_config_name.setFocus()

        self.data_config = common_util.load_data_config()

        self.switch_has_time.checkedChanged.connect(self.switch_toggled)
        self.line_data_config_name.editingFinished.connect(self.verify_data_config_name)
        self.btn_cancel.clicked.connect(self.close)
        self.btn_confirm.clicked.connect(self.add_data_config)

    def add_data_config(self):
        """ 添加数据表配置 """
        # 常规配置缺失时, 提示错误
        if not self.line_data_config_name.text() or not self.line_channel_id.text() or not self.line_type_id.text() or not self.line_sheet.text() or not self.line_customer_col.text():
            InfoBar.error(
                title='配置错误',
                content="配置项不能为空!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif self.line_data_config_name.text().__contains__(' ') or self.line_channel_id.text().__contains__(' ') or self.line_type_id.text().__contains__(' ') or self.line_sheet.text().__contains__(' ') or self.line_customer_col.text().__contains__(' '):
            InfoBar.error(
                title='配置错误',
                content="配置项不能含有空白字符!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        # 时间列配置缺失时, 提示错误
        elif self.switch_has_time.checked and (not self.line_time_col.text() or not self.line_time_format.text()):
            InfoBar.error(
                title='配置错误',
                content="[有时间列] 时间列和时间格式配置不能为空!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        # 配置名重复时, 提示错误
        elif list(self.data_config.keys()).__contains__(self.line_data_config_name.text()) and self.line_data_config_name.isEnabled():
            InfoBar.error(
                title='配置错误',
                content="配置名不能重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif self.line_customer_col.text().replace("，", ",").split(",").__contains__(''):
            InfoBar.error(
                title='配置错误',
                content="客户名有空白, 请检查多余的逗号!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif len(self.line_customer_col.text().replace("，", ",").split(",")) != len(set(self.line_customer_col.text().replace("，", ",").split(","))):
            InfoBar.error(
                title='配置错误',
                content="不允许客户字段名重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        else:
            self.data_config[f'{self.line_data_config_name.text()}'] = {
                "channel_id": self.line_channel_id.text(),
                "type_id": self.line_type_id.text(),
                "sheet": self.line_sheet.text(),
                "has_time": self.switch_has_time.isChecked(),
                "time_col": self.line_time_col.text(),
                "time_format": self.line_time_format.text(),
                "customer_col": self.line_customer_col.text().replace("，", ",").split(","),
            }
            common_util.save_data_config(self.data_config)
            self.closed.emit()
            self.close()

    def switch_toggled(self):
        """ 设置是否存在时间列 """
        if self.switch_has_time.isChecked():
            self.line_time_col.setEnabled(True)
            self.line_time_format.setEnabled(True)
        else:
            self.line_time_col.setText('')
            self.line_time_format.setText('')
            self.line_time_col.setEnabled(False)
            self.line_time_format.setEnabled(False)

    def verify_data_config_name(self):
        if list(self.data_config.keys()).__contains__(self.line_data_config_name.text()) and self.line_data_config_name.isEnabled():
            InfoBar.error(
                title='配置错误',
                content="配置名不能重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
