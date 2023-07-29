import markdown
from PyQt6.QtCore import QFileSystemWatcher
from PyQt6.QtWidgets import QWidget

from ui.help_ui import Ui_help_widget
from util import common_util


class HelpView(QWidget, Ui_help_widget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.help_watcher = QFileSystemWatcher([common_util.get_real_path('resources', 'help.md')])
        self.help_watcher.fileChanged.connect(self.help_changed)
        self.help_changed()

    def help_changed(self):
        with open(common_util.get_real_path('resources', 'help.md'), mode='r', encoding='utf-8') as md_file:
            md_file_text = md_file.read()
            md_file_text = md_file_text.replace('img_dir', common_util.get_real_path('resources', 'img'))
            md_html = markdown.markdown(md_file_text)
            self.help_md.setHtml(md_html)
