import markdown
from PyQt6.QtWidgets import QWidget

from ui.help_ui import Ui_help_widget
from util.common_util import get_real_path


class HelpView(QWidget, Ui_help_widget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        with open(get_real_path('resources', 'help.md'), mode='r', encoding='utf-8') as md_file:
            md_html = markdown.markdown(md_file.read())
            self.help_md.setHtml(md_html)
