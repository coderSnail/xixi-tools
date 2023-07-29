import sys

from PyQt6.QtWidgets import QApplication

from view.xixi_view import XixiView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    xixi = XixiView()
    xixi.show()
    sys.exit(app.exec())
