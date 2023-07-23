from PyQt6.QtCore import pyqtSignal, Qt, QRegularExpression
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QListWidgetItem, QSizePolicy
from qfluentwidgets import InfoBar, InfoBarPosition, LineEdit, PushButton, FluentIcon, Theme, Dialog

from ui.add_company_config_ui import Ui_company_config_widget
from util import common_util
from util.common_util import get_real_path
from view.add_company_view import AddCompanyView


class AddCompanyConfigView(QWidget, Ui_company_config_widget):
    closed = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(get_real_path('resources', 'xixi.ico')))
        self.list_company.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.line_group.setFocus()

        self.company_config = common_util.load_company_config()
        if self.sender().objectName().__contains__('edit_company_'):
            self.companies = self.company_config[self.sender().objectName().replace('edit_company_', '')]
        else:
            self.companies = []

        self.line_group.editingFinished.connect(self.verify_company_config_group)
        self.btn_add_company.clicked.connect(self.show_add_company)
        self.btn_confirm.clicked.connect(self.add_company_config)

    def show_add_company(self):
        self.add_company_window = AddCompanyView(companies=self.companies)
        self.add_company_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.add_company_window.setWindowTitle("新增 - 公司")
        self.add_company_window.line_company_name.setFocus()
        self.add_company_window.closed.connect(self.add_company)
        self.add_company_window.show()

    def add_company_config(self):
        companies = []
        for item in self.list_company.findChildren(LineEdit, QRegularExpression("line_company[\\d\\S]*")):
            companies.append(item.text())
        if not companies:
            InfoBar.error(
                title='配置错误',
                content="至少添加一个公司名!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif self.line_group.text().__contains__(' '):
            InfoBar.error(
                title='配置错误',
                content="集团名不能含有空白字符!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif not self.line_group.text() or companies.__contains__(''):
            # 常规配置缺失错误
            InfoBar.error(
                title='配置错误',
                content="所有配置项不能为空!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif list(self.company_config.keys()).__contains__(self.line_group.text()) and self.line_group.isEnabled():
            # 集团名重复
            InfoBar.error(
                title='配置错误',
                content="集团名不能重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif len(companies) != len(set(companies)):
            # 公司名重复
            InfoBar.error(
                title='配置错误',
                content="公司名不能重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        else:
            print(self.company_config)
            self.companies = companies
            self.company_config[self.line_group.text()] = self.companies
            common_util.save_company_config(self.company_config)
            self.closed.emit()
            self.close()

    def add_company(self, company_name):
        # 添加公司名
        self.companies.append(company_name)
        self.load_company()

    def delete_company(self):
        # 删除公司名
        company = self.sender().objectName().replace('delete_company_', '')
        title = '确认删除?'
        content = f"""是否删除\n公司 - {company}"""
        w = Dialog(title, content, self)
        w.yesButton.setText('确认')
        w.cancelButton.setText('取消')
        if w.exec():
            self.companies.remove(company)
            self.load_company()

    def edit_company_finished(self):
        print(self.sender().objectName())

    def load_company(self):
        """ 添加公司编辑行 """
        self.list_company.clear()
        for company in self.companies:
            row_widget = QWidget(self.list_company)
            row_widget.setStyleSheet("QWidget {background-color: #fff;}")
            row_widget.setFixedHeight(34)
            h_layout = QHBoxLayout()
            h_layout.setContentsMargins(0, 0, 5, 0)
            h_layout.setSpacing(3)
            line_company = LineEdit(row_widget)
            line_company.setObjectName(f'line_company_{company}')
            line_company.editingFinished.connect(self.edit_company_finished)
            line_company.setText(company)
            btn_delete_company = PushButton(row_widget)
            btn_delete_company.setObjectName(f'delete_company_{company}')
            btn_delete_company.clicked.connect(self.delete_company)
            btn_delete_company.setIcon(FluentIcon.DELETE.icon(Theme.AUTO, QColor(255, 130, 130)))
            btn_delete_company.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            btn_delete_company.setStyleSheet("""
                        PushButton{
                            background-color: #fff;
                            border: 1px solid rgba(255, 170, 170, 1);
                            border-radius: 5px;
                            padding: 5px 0px 5px 5px;
                            outline: none;
                        }
                        PushButton:hover{
                            background: rgba(255, 170, 170, 0.2);
                        }
                        PushButton:pressed{
                            background: rgba(255, 170, 170, 0.7);
                        }
                        """)
            h_layout.addWidget(line_company)
            h_layout.addWidget(btn_delete_company)
            row_widget.setLayout(h_layout)

            item = QListWidgetItem(self.list_company)
            self.list_company.setItemWidget(item, row_widget)
            line_company.setFocus()

    def verify_company_config_group(self):
        if list(self.company_config.keys()).__contains__(self.line_group.text()) and self.line_group.isEnabled():
            InfoBar.error(
                title='配置错误',
                content="集团名不能重复!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
        elif self.line_group.text().__contains__(' '):
            InfoBar.error(
                title='配置错误',
                content="集团名不能含有空白字符!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP_RIGHT,
                duration=2000,
                parent=self
            )
