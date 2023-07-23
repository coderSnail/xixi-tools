from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from qfluentwidgets import NavigationItemPosition

from ui.xixi_ui import Ui_xixi
from util.common_util import get_real_path
from view.config_view import ConfigView
from view.help_view import HelpView
from view.home_view import HomeView


class XixiView(QWidget, Ui_xixi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(get_real_path('resources', 'xixi.ico')))

        self.home_view = HomeView(self)
        self.config_view = ConfigView(self)
        self.help_view = HelpView(self)

        self.add_sub_interface(self.home_view, FluentIcon.HOME, '主页', selected_icon=FluentIcon.HOME_FILL)
        self.add_sub_interface(self.config_view, FluentIcon.SETTING, '配置')
        self.add_sub_interface(self.help_view, FluentIcon.HELP, '帮助')

        self.nav_bar.setCurrentItem(self.home_view.objectName())
        self.stacked_widget.setCurrentWidget(self.home_view)

    def add_sub_interface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, selected_icon=None):
        """ add sub interface """
        self.stacked_widget.addWidget(interface)
        self.nav_bar.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switch_to(interface),
            selectedIcon=selected_icon,
            position=position,
        )

    def switch_to(self, widget):
        self.stacked_widget.setCurrentWidget(widget)
