# Form implementation generated from reading ui file 'xixi.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_xixi(object):
    def setupUi(self, xixi):
        xixi.setObjectName("xixi")
        xixi.resize(1265, 750)
        xixi.setStyleSheet("QWidget {\n"
"    background-color: #fff;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(xixi)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nav_bar = NavigationBar(parent=xixi)
        self.nav_bar.setMaximumSize(QtCore.QSize(72, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.nav_bar.setFont(font)
        self.nav_bar.setStyleSheet("NavigationBar {\n"
"    border: 1px solid #ddd;\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"NavigationPanel[menu=true] {\n"
"    background-color: rgb(243, 243, 243);\n"
"    border: 1px solid rgb(229, 229, 229);\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}\n"
"\n"
"NavigationPanel[menu=false] {\n"
"    background-color: transparent;\n"
"    border: 1px solid transparent;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"}\n"
"\n"
"QScrollArea, #scrollWidget {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"")
        self.nav_bar.setObjectName("nav_bar")
        self.horizontalLayout.addWidget(self.nav_bar)
        self.stacked_widget = QtWidgets.QStackedWidget(parent=xixi)
        self.stacked_widget.setObjectName("stacked_widget")
        self.horizontalLayout.addWidget(self.stacked_widget)

        self.retranslateUi(xixi)
        QtCore.QMetaObject.connectSlotsByName(xixi)

    def retranslateUi(self, xixi):
        _translate = QtCore.QCoreApplication.translate
        xixi.setWindowTitle(_translate("xixi", "xixi工具箱 - 数据筛选转换工具"))
from qfluentwidgets import NavigationBar
