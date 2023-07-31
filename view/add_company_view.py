from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget
from qfluentwidgets import InfoBarPosition, InfoBar

from ui.add_company_ui import Ui_add_company_widget
from util import common_util
from util.common_util import get_real_path


class AddCompanyView(QWidget, Ui_add_company_widget):
    closed = pyqtSignal(str)

    def __init__(self, parent=None, companies=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(get_real_path('xixi.ico')))
        self.line_company_name.setFocus()
        self.companies = companies

        self.btn_add_company_name.clicked.connect(self.add_company)

    def add_company(self):
        if self.line_company_name.text().__contains__(' '):
            InfoBar.error(
                title='添加错误',
                content="公司名不能含有空白字符!",
                orient=Qt.Orientation.Vertical,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )
        elif self.line_company_name.text():
            company_config = common_util.load_company_config()
            all_companies = []
            for key in company_config.keys():
                all_companies.extend(company_config[key])

            if all_companies.__contains__(self.line_company_name.text()):
                InfoBar.error(
                    title='添加错误',
                    content="同个公司只能添加在一个集团下!",
                    orient=Qt.Orientation.Vertical,
                    isClosable=False,  # disable close button
                    position=InfoBarPosition.TOP,
                    duration=2000,
                    parent=self
                )
            else:
                self.closed.emit(self.line_company_name.text())
                self.close()
        else:
            InfoBar.error(
                title='添加错误',
                content="公司名不能为空!",
                orient=Qt.Orientation.Vertical,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )