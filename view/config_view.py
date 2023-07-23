from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy
from qfluentwidgets import PushButton, BodyLabel, CheckBox, FluentIcon, Theme, MessageBox, Dialog

from ui.config_ui import Ui_config_widget
from util import common_util
from view.add_company_config_view import AddCompanyConfigView
from view.add_data_config_view import AddDataConfigView


class ConfigView(QWidget, Ui_config_widget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.data_config = common_util.load_data_config()
        self.show_data_config()
        self.company_config = common_util.load_company_config()
        self.show_company_config()

        self.btn_add_data_config.clicked.connect(self.add_data_config)
        self.btn_add_company_config.clicked.connect(self.add_company_config)

    def add_data_config(self):
        self.add_data_config_window = AddDataConfigView()
        self.add_data_config_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.add_data_config_window.setWindowTitle("新增 - 源数据表配置")
        self.add_data_config_window.closed.connect(self.show_data_config)
        self.add_data_config_window.show()

    def add_company_config(self):
        self.add_company_config_window = AddCompanyConfigView()
        self.add_company_config_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.add_company_config_window.setWindowTitle("新增 - [集团-公司]配置")
        self.add_company_config_window.line_group.setFocus()
        self.add_company_config_window.closed.connect(self.show_company_config)
        self.add_company_config_window.show()

    def show_data_config(self):
        widget_list = [['配置名', '渠道标识', '类型标识', 'Sheet表名', '有时间列', '时间列[表字段名]', '时间格式', '客户名[表字段名]', '操作']]
        self.data_config = common_util.load_data_config()

        for row in self.data_config.keys():
            row_list = [row]
            for col in self.data_config[row].keys():
                row_list.append(self.data_config[row][col])
            row_list.append(11)  # 用整数标识操作按钮
            widget_list.append(row_list)

        self.create_group_table(widget_list, self.widget_data)

    def show_company_config(self):
        widget_list = [['集团名', '客户名', '操作']]
        self.company_config = common_util.load_company_config()

        for row in self.company_config.keys():
            row_list = [row, ','.join(self.company_config[row]), 11]  # 用整数标识操作按钮
            widget_list.append(row_list)
        self.create_group_table(widget_list, self.widget_company)

    def operate(self):
        sender = self.sender().objectName()
        if sender.__contains__('edit_data'):
            # 编辑源数据表配置
            self.edit_data_config_window = AddDataConfigView()
            self.edit_data_config_window.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.edit_data_config_window.setWindowTitle("修改 - 源数据表配置")
            self.edit_data_config_window.line_data_config_name.setEnabled(False)
            self.edit_data_config_window.closed.connect(self.show_data_config)

            # 回显数据
            row_data = self.data_config[sender.replace('edit_data_', '')]
            self.edit_data_config_window.line_data_config_name.setText(sender.replace('edit_data_', ''))
            self.edit_data_config_window.line_channel_id.setText(row_data['channel_id'])
            self.edit_data_config_window.line_type_id.setText(row_data['type_id'])
            self.edit_data_config_window.line_sheet.setText(row_data['sheet'])
            self.edit_data_config_window.switch_has_time.setChecked(row_data['has_time'])
            self.edit_data_config_window.line_time_col.setText(row_data['time_col'])
            self.edit_data_config_window.line_time_format.setText(row_data['time_format'])
            self.edit_data_config_window.line_customer_col.setText(','.join(row_data['customer_col']))

            self.edit_data_config_window.show()
        elif sender.__contains__('delete_data'):
            title = '确认删除?'
            content = f"""是否删除\n[源数据表]配置 - {sender.replace('delete_data_', '')}"""
            w = Dialog(title, content, self)
            w.yesButton.setText('确认')
            w.cancelButton.setText('取消')
            if w.exec():
                del self.data_config[sender.replace('delete_data_', '')]
                common_util.save_data_config(self.data_config)
        elif sender.__contains__('edit_company'):
            self.edit_company_config_window = AddCompanyConfigView()
            self.edit_company_config_window.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.edit_company_config_window.setWindowTitle("修改 - [集团-公司]配置")
            self.edit_company_config_window.line_group.setEnabled(False)
            self.edit_company_config_window.closed.connect(self.show_company_config)
            # 回显数据
            self.edit_company_config_window.line_group.setText(sender.replace('edit_company_', ''))
            self.edit_company_config_window.load_company()

            self.edit_company_config_window.show()
        elif sender.__contains__('delete_company'):
            title = '确认删除?'
            content = f"""是否删除\n[集团-公司]配置 - {sender.replace('delete_company_', '')}"""
            w = Dialog(title, content, self)
            w.yesButton.setText('确认')
            w.cancelButton.setText('取消')
            if w.exec():
                del self.company_config[sender.replace('delete_company_', '')]
                common_util.save_company_config(self.company_config)

        self.show_data_config()
        self.show_company_config()

    def create_group_table(self, widget_list, _widget):
        if _widget.layout().count():
            _widget.layout().itemAt(_widget.layout().count() - 1).widget().hide()

        group_box = QtWidgets.QGroupBox(parent=self.widget_data)
        group_box.setStyleSheet("QGroupBox {\n"
                                "    border: 1px solid #ddd;\n"
                                "    border-radius: 10px;\n"
                                "}")
        group_box.setTitle("")
        grid_layout = QtWidgets.QGridLayout(group_box)
        grid_layout.setContentsMargins(6, 10, 6, 6)
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(10)
        group_box.setLayout(grid_layout)
        _widget.layout().addWidget(group_box)
        group_box.show()

        for row, widget_item in enumerate(widget_list):
            row_height = 40
            for col, item in enumerate(widget_item):
                if isinstance(item, str) or isinstance(item, list):
                    if isinstance(item, list):
                        item = ','.join(item)
                    label = BodyLabel(group_box)
                    label.setText(item)
                    label.setFixedHeight(row_height)
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    if row == 0:
                        label.setStyleSheet("BodyLabel {border-bottom: 2px solid #ccc; font-weight: bold; padding-left: 5px; padding-right: 5px;}")
                    elif col == 0:
                        label.setStyleSheet(
                            "BodyLabel {border-bottom: 1px solid #ddd; border-left: 1px solid #ddd; border-top: 1px solid #ddd; border-top-left-radius: 5px; border-bottom-left-radius: 5px; padding-left: 5px; padding-right: 5px;}")
                    elif col == len(widget_item) - 1:
                        label.setStyleSheet(
                            "BodyLabel {border-bottom: 1px solid #ddd; border-right: 1px solid #ddd; border-top: 1px solid #ddd; border-top-right-radius: 5px; border-bottom-right-radius: 5px; padding-left: 5px; padding-right: 5px;}")
                    else:
                        label.setStyleSheet("BodyLabel {border-bottom: 1px solid #ddd; border-top: 1px solid #ddd; padding-left: 5px; padding-right: 5px;}")
                    group_box.layout().addWidget(label, row, col, 1, 1)

                if isinstance(item, bool):
                    # checkbox 居中设置
                    temp_widget = QWidget(group_box)
                    temp_widget.setObjectName(f"temp_widget_{widget_item[0]}")
                    temp_widget.setFixedWidth(80)
                    temp_widget.setStyleSheet(f"""
                    #temp_widget_{row} {{
                        border-bottom: 1px solid #ddd;
                        border-top: 1px solid #ddd;
                    }}
                    """)
                    h_layout = QHBoxLayout()
                    h_layout.setContentsMargins(0, 0, 0, 0)
                    spacer_item = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
                    h_layout.addItem(spacer_item)
                    check_box = CheckBox(temp_widget)
                    check_box.setChecked(item)
                    check_box.setEnabled(False)
                    check_box.setFixedHeight(row_height - 2)
                    check_box.setStyleSheet("""
                    CheckBox:disabled {
                        font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';
                        outline: none;
                    }
                    CheckBox::indicator:disabled {
                        width: 18px;
                        height: 18px;
                        border-radius: 5px;
                        border: 1px solid rgba(0, 0, 0, 0.48);
                        background-color: rgba(0, 0, 0, 0.022);
                    }
                    CheckBox::indicator:checked:disabled,
                    CheckBox::indicator:indeterminate:disabled {
                        border: 1px solid #009faa;
                        background-color: #009faa;
                    }
                    """)

                    h_layout.addWidget(check_box)
                    h_layout.addItem(spacer_item)
                    temp_widget.setLayout(h_layout)

                    group_box.layout().addWidget(temp_widget, row, col, 1, 1)

                if item == 11:
                    button_widget = QWidget(group_box)
                    button_widget.setObjectName(f"{_widget.objectName()}_{widget_item[0]}")
                    button_widget.setFixedWidth(80)
                    button_widget.setStyleSheet(f"""
                    #{_widget.objectName()}_{widget_item[0]} {{
                        border-bottom: 1px solid #ddd;
                        border-right: 1px solid #ddd;
                        border-top: 1px solid #ddd;
                        border-top-right-radius: 5px;
                        border-bottom-right-radius: 5px;
                        padding-left: 5px;
                        padding-right: 5px;
                    }}
                    """)
                    h_layout = QHBoxLayout()
                    h_layout.setContentsMargins(5, 0, 5, 0)
                    h_layout.setSpacing(3)

                    btn_edit = PushButton()
                    btn_edit.setObjectName(f'edit_{_widget.objectName().replace("widget_", "")}_{widget_item[0]}')
                    btn_edit.clicked.connect(self.operate)
                    btn_edit.setIcon(FluentIcon.EDIT.icon(Theme.AUTO, QColor(0, 159, 170)))
                    btn_edit.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                    btn_edit.setStyleSheet("""
                    PushButton {
                        background-color: #fff;
                        border: 1px solid rgba(0, 159, 170, 0.6);
                        border-radius: 5px;
                        padding: 5px 0px 5px 5px;
                        outline: none;
                    }
                    PushButton:hover {
                        background: rgba(0, 159, 170, 0.1);
                    }
                    PushButton:pressed {
                        background: rgba(0, 159, 170, 0.4);
                    }
                    """)

                    btn_delete = PushButton()
                    btn_delete.setObjectName(f'delete_{_widget.objectName().replace("widget_", "")}_{widget_item[0]}')
                    btn_delete.clicked.connect(self.operate)
                    btn_delete.setIcon(FluentIcon.DELETE.icon(Theme.AUTO, QColor(255, 130, 130)))
                    btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                    btn_delete.setStyleSheet("""
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

                    h_layout.addWidget(btn_edit)
                    h_layout.addWidget(btn_delete)
                    button_widget.setLayout(h_layout)

                    group_box.layout().addWidget(button_widget, row, col, 1, 1)
