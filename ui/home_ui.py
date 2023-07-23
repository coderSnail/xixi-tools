# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_home_widget(object):
    def setupUi(self, home_widget):
        home_widget.setObjectName("home_widget")
        home_widget.resize(1049, 673)
        home_widget.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(home_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_import = PrimaryPushButton(parent=home_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_import.sizePolicy().hasHeightForWidth())
        self.btn_import.setSizePolicy(sizePolicy)
        self.btn_import.setStyleSheet("PushButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"PrimaryPushButton {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}")
        self.btn_import.setObjectName("btn_import")
        self.horizontalLayout_6.addWidget(self.btn_import)
        self.btn_analyse = PrimaryPushButton(parent=home_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_analyse.sizePolicy().hasHeightForWidth())
        self.btn_analyse.setSizePolicy(sizePolicy)
        self.btn_analyse.setStyleSheet("PushButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"PrimaryPushButton {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}")
        self.btn_analyse.setObjectName("btn_analyse")
        self.horizontalLayout_6.addWidget(self.btn_analyse)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.BodyLabel_6 = BodyLabel(parent=home_widget)
        self.BodyLabel_6.setMinimumSize(QtCore.QSize(0, 32))
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.horizontalLayout_6.addWidget(self.BodyLabel_6)
        self.combo_month = ComboBox(parent=home_widget)
        self.combo_month.setMinimumSize(QtCore.QSize(75, 32))
        self.combo_month.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.combo_month.setFont(font)
        self.combo_month.setText("")
        self.combo_month.setCheckable(False)
        self.combo_month.setChecked(False)
        self.combo_month.setObjectName("combo_month")
        self.horizontalLayout_6.addWidget(self.combo_month)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.qwidget1 = QtWidgets.QWidget(parent=home_widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.qwidget1.setFont(font)
        self.qwidget1.setStyleSheet("QWidget#qwidget1 {\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 10px;\n"
"} ")
        self.qwidget1.setObjectName("qwidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.qwidget1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StrongBodyLabel = StrongBodyLabel(parent=self.qwidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StrongBodyLabel.sizePolicy().hasHeightForWidth())
        self.StrongBodyLabel.setSizePolicy(sizePolicy)
        self.StrongBodyLabel.setMinimumSize(QtCore.QSize(0, 32))
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.horizontalLayout.addWidget(self.StrongBodyLabel)
        self.label_data_dir = BodyLabel(parent=self.qwidget1)
        self.label_data_dir.setMinimumSize(QtCore.QSize(0, 32))
        self.label_data_dir.setText("")
        self.label_data_dir.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_data_dir.setObjectName("label_data_dir")
        self.horizontalLayout.addWidget(self.label_data_dir)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.list_widget_file = ListWidget(parent=self.qwidget1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.list_widget_file.setFont(font)
        self.list_widget_file.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.list_widget_file.setStyleSheet("ListView,\n"
"ListWidget {\n"
"    background: #fff;\n"
"    outline: none;\n"
"    /* border: none; */\n"
"    border-top: 1px solid #ddd;\n"
"    /* font: 13px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"}\n"
"\n"
"ListView::item,\n"
"ListWidget::item {\n"
"    background: #fff;\n"
"    border: 0px;\n"
"    padding-left: 11px;\n"
"    padding-right: 11px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"ListView::indicator,\n"
"ListWidget::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"ListView::indicator:hover,\n"
"ListWidget::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"ListView::indicator:pressed,\n"
"ListWidget::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}\n"
"\n"
"ListView::indicator:checke,\n"
"ListWidget::indicator:checked,\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"ListView::indicator:checked,\n"
"ListWidget::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:checked:hove,\n"
"ListWidget::indicator:checked:hover,\n"
"ListView::indicator:indeterminate:hover,\n"
"ListWidget::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"ListView::indicator:checked:presse,\n"
"ListWidget::indicator:checked:pressed,\n"
"ListView::indicator:indeterminate:pressed,\n"
"ListWidget::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"ListView::indicator:disabled,\n"
"ListWidget::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"ListView::indicator:checked:disable,\n"
"ListWidget::indicator:checked:disabled,\n"
"ListView::indicator:indeterminate:disabled,\n"
"ListWidget::indicator:indeterminate:disabled {\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}")
        self.list_widget_file.setAlternatingRowColors(False)
        self.list_widget_file.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.NoSelection)
        self.list_widget_file.setResizeMode(QtWidgets.QListView.ResizeMode.Fixed)
        self.list_widget_file.setObjectName("list_widget_file")
        self.verticalLayout_4.addWidget(self.list_widget_file)
        self.verticalLayout_5.addWidget(self.qwidget1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.calendar_start = CalendarPicker(parent=home_widget)
        self.calendar_start.setMinimumSize(QtCore.QSize(120, 0))
        self.calendar_start.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.calendar_start.setFont(font)
        self.calendar_start.setStyleSheet("#titleButton {\n"
"    font: 14px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    font-weight: 500;\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding-left: 8px;\n"
"    text-align: left;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#titleButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#titleButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"\n"
"#titleButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"#weekDayLabel {\n"
"    font: 12px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    font-weight: 500;\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#weekDayGroup {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CalendarViewBase {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"ScrollViewBase {\n"
"    border: none;\n"
"    padding: 0px 1px 0px 1px;\n"
"    border-bottom-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-top: 1px solid rgb(240, 240, 240);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CalendarPicker {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    font: 14px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    padding: 5px 32px 6px 12px;\n"
"    outline: none;\n"
"    text-align: left;\n"
"}\n"
"\n"
"\n"
"CalendarPicker:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"CalendarPicker:pressed {\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"CalendarPicker:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"CalendarPicker[hasDate=true] {\n"
"    color: black;\n"
"}")
        self.calendar_start.setObjectName("calendar_start")
        self.horizontalLayout_7.addWidget(self.calendar_start)
        self.calendar_end = CalendarPicker(parent=home_widget)
        self.calendar_end.setMinimumSize(QtCore.QSize(120, 0))
        self.calendar_end.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.calendar_end.setFont(font)
        self.calendar_end.setStyleSheet("#titleButton {\n"
"    font: 14px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    font-weight: 500;\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    margin: 0;\n"
"    padding-left: 8px;\n"
"    text-align: left;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#titleButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"}\n"
"\n"
"#titleButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"}\n"
"\n"
"#titleButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"#weekDayLabel {\n"
"    font: 12px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    font-weight: 500;\n"
"    color: black;\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#weekDayGroup {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CalendarViewBase {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgba(0, 0, 0, 0.1);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"ScrollViewBase {\n"
"    border: none;\n"
"    padding: 0px 1px 0px 1px;\n"
"    border-bottom-left-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    border-top: 1px solid rgb(240, 240, 240);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"CalendarPicker {\n"
"    color: rgba(0, 0, 0, 0.6063);\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    font: 14px  \'Segoe UI\', \'Microsoft YaHei\', \'PingFang SC\';\n"
"    padding: 5px 32px 6px 12px;\n"
"    outline: none;\n"
"    text-align: left;\n"
"}\n"
"\n"
"\n"
"CalendarPicker:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"CalendarPicker:pressed {\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"CalendarPicker:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"CalendarPicker[hasDate=true] {\n"
"    color: black;\n"
"}")
        self.calendar_end.setObjectName("calendar_end")
        self.horizontalLayout_7.addWidget(self.calendar_end)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.btn_export = PrimaryPushButton(parent=home_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setStyleSheet("PushButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"PrimaryPushButton {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover {\n"
"    background-color: #00a7b3;\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}")
        self.btn_export.setObjectName("btn_export")
        self.horizontalLayout_7.addWidget(self.btn_export)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.qwidget2 = QtWidgets.QWidget(parent=home_widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.qwidget2.setFont(font)
        self.qwidget2.setStyleSheet("QWidget#qwidget2 {\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 10px;\n"
"} ")
        self.qwidget2.setObjectName("qwidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.qwidget2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.qwidget2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.check_box_select_all = CheckBox(parent=self.widget_2)
        self.check_box_select_all.setMinimumSize(QtCore.QSize(29, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        self.check_box_select_all.setFont(font)
        self.check_box_select_all.setObjectName("check_box_select_all")
        self.horizontalLayout_9.addWidget(self.check_box_select_all)
        self.line_edit_search = SearchLineEdit(parent=self.widget_2)
        self.line_edit_search.setMinimumSize(QtCore.QSize(120, 32))
        self.line_edit_search.setMaximumSize(QtCore.QSize(200, 32))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        font.setBold(False)
        self.line_edit_search.setFont(font)
        self.line_edit_search.setObjectName("line_edit_search")
        self.horizontalLayout_9.addWidget(self.line_edit_search)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_2)
        self.list_widget_company = ListWidget(parent=self.qwidget2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.list_widget_company.setFont(font)
        self.list_widget_company.setStyleSheet("ListView,\n"
"ListWidget {\n"
"    background: transparent;\n"
"    outline: none;\n"
"    /* border: none; */\n"
"    border-top: 1px solid #ddd;\n"
"    /* font: 13px \'Segoe UI\', \'Microsoft YaHei\'; */\n"
"    selection-background-color: transparent;\n"
"    alternate-background-color: transparent;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"}\n"
"\n"
"ListView::item,\n"
"ListWidget::item {\n"
"    background: transparent;\n"
"    border: 0px;\n"
"    padding-left: 11px;\n"
"    padding-right: 11px;\n"
"    height: 35px;\n"
"}\n"
"\n"
"\n"
"ListView::indicator,\n"
"ListWidget::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgba(0, 0, 0, 0.48);\n"
"    background-color: rgba(0, 0, 0, 0.022);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"ListView::indicator:hover,\n"
"ListWidget::indicator:hover {\n"
"    border: 1px solid rgba(0, 0, 0, 0.56);\n"
"    background-color: rgba(0, 0, 0, 0.05);\n"
"}\n"
"\n"
"ListView::indicator:pressed,\n"
"ListWidget::indicator:pressed {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: rgba(0, 0, 0, 0.12);\n"
"}\n"
"\n"
"ListView::indicator:checke,\n"
"ListWidget::indicator:checked,\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    border: 1px solid #009faa;\n"
"    background-color: #009faa;\n"
"}\n"
"\n"
"ListView::indicator:checked,\n"
"ListWidget::indicator:checked {\n"
"    image: url(:/qfluentwidgets/images/check_box/Accept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:indeterminate,\n"
"ListWidget::indicator:indeterminate {\n"
"    image: url(:/qfluentwidgets/images/check_box/PartialAccept_white.svg);\n"
"}\n"
"\n"
"ListView::indicator:checked:hove,\n"
"ListWidget::indicator:checked:hover,\n"
"ListView::indicator:indeterminate:hover,\n"
"ListWidget::indicator:indeterminate:hover {\n"
"    border: 1px solid #00a7b3;\n"
"    background-color: #00a7b3;\n"
"}\n"
"\n"
"ListView::indicator:checked:presse,\n"
"ListWidget::indicator:checked:pressed,\n"
"ListView::indicator:indeterminate:pressed,\n"
"ListWidget::indicator:indeterminate:pressed {\n"
"    border: 1px solid #3eabb3;\n"
"    background-color: #3eabb3;\n"
"}\n"
"\n"
"ListView::indicator:disabled,\n"
"ListWidget::indicator:disabled {\n"
"    border: 1px solid rgba(0, 0, 0, 0.27);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"ListView::indicator:checked:disable,\n"
"ListWidget::indicator:checked:disabled,\n"
"ListView::indicator:indeterminate:disabled,\n"
"ListWidget::indicator:indeterminate:disabled {\n"
"    border: 1px solid rgb(199, 199, 199);\n"
"    background-color: rgb(199, 199, 199);\n"
"}")
        self.list_widget_company.setAlternatingRowColors(False)
        self.list_widget_company.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.list_widget_company.setObjectName("list_widget_company")
        self.verticalLayout_3.addWidget(self.list_widget_company)
        self.verticalLayout_2.addWidget(self.qwidget2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_log = TextEdit(parent=home_widget)
        self.text_log.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
"    color: black;\n"
"    background-color: #fff;\n"
"    border: 1px solid #ddd;\n"
"    /* font: 14px \"Segoe UI\", \"Microsoft YaHei\"; */\n"
"    padding: 0px 10px;\n"
"    selection-background-color: #00a7b3;\n"
"}\n"
"\n"
"TextEdit,\n"
"PlainTextEdit {\n"
"    padding: 0px 0px 0px 10px;\n"
"}")
        self.text_log.setReadOnly(True)
        self.text_log.setObjectName("text_log")
        self.horizontalLayout_2.addWidget(self.text_log)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(home_widget)
        QtCore.QMetaObject.connectSlotsByName(home_widget)

    def retranslateUi(self, home_widget):
        _translate = QtCore.QCoreApplication.translate
        home_widget.setWindowTitle(_translate("home_widget", "数据导出"))
        self.btn_import.setText(_translate("home_widget", "导入源表"))
        self.btn_analyse.setText(_translate("home_widget", "分析数据"))
        self.BodyLabel_6.setText(_translate("home_widget", "快捷选择整月:"))
        self.combo_month.setToolTip(_translate("home_widget", "在源数据表所有日期包含的月份中快速选取整月范围"))
        self.StrongBodyLabel.setText(_translate("home_widget", "源数据表目录: "))
        self.calendar_start.setToolTip(_translate("home_widget", "选取导出数据的开始日期 (包含)"))
        self.calendar_start.setText(_translate("home_widget", "开始日期"))
        self.calendar_end.setToolTip(_translate("home_widget", "选取导出数据的结束日期 (包含)"))
        self.calendar_end.setText(_translate("home_widget", "结束日期"))
        self.btn_export.setText(_translate("home_widget", "导出数据"))
        self.check_box_select_all.setText(_translate("home_widget", "选择全部"))
        self.text_log.setHtml(_translate("home_widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\',\'Microsoft YaHei\',\'PingFang SC\'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
from qfluentwidgets import BodyLabel, CalendarPicker, CheckBox, ComboBox, ListWidget, PrimaryPushButton, SearchLineEdit, StrongBodyLabel, TextEdit