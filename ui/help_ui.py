# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_help_widget(object):
    def setupUi(self, help_widget):
        help_widget.setObjectName("help_widget")
        help_widget.resize(1050, 581)
        self.horizontalLayout = QtWidgets.QHBoxLayout(help_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.help_md = TextEdit(parent=help_widget)
        self.help_md.setStyleSheet("LineEdit, TextEdit, PlainTextEdit {\n"
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
        self.help_md.setReadOnly(True)
        self.help_md.setObjectName("help_md")
        self.horizontalLayout.addWidget(self.help_md)

        self.retranslateUi(help_widget)
        QtCore.QMetaObject.connectSlotsByName(help_widget)

    def retranslateUi(self, help_widget):
        _translate = QtCore.QCoreApplication.translate
        help_widget.setWindowTitle(_translate("help_widget", "帮助文件"))
from qfluentwidgets import TextEdit
