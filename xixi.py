import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from util.common_util import get_real_path
from view.xixi_view import XixiView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(get_real_path('resources', 'xixi.ico')))
    xixi = XixiView()
    xixi.show()
    sys.exit(app.exec())
