import calendar
from datetime import datetime
from enum import Enum

from PyQt6.QtCore import QDate, pyqtSignal, QFileSystemWatcher, Qt
from PyQt6.QtWidgets import QWidget, QFileDialog, QListWidgetItem
from qfluentwidgets import ToolTipFilter, ToolTipPosition, TeachingTip, InfoBarIcon, TeachingTipTailPosition, InfoBar, InfoBarPosition

from ui.home_ui import Ui_home_widget
from util import common_util
from view.file_item_view import FileItemView
from xixi_enum import Status


class HomeView(QWidget, Ui_home_widget):
    # 软件状态信号
    status_signal = pyqtSignal(Enum)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.status = Status.INIT
        self.start_date = None  # 开始日期
        self.end_date = None  # 结束日期

        self.data_dir = ''  # 源数据表文件路径
        self.data_files = []  # 源数据表
        self.data_config = common_util.load_data_config()  # 源数据表配置
        self.file_item_widgets = []  # 文件列表行控件

        self.companies_checked = []  # 选中的集团名
        self.companies = []  # 分析后所有源数据表存在的集团名(公司映射后的)
        self.company_config = common_util.load_company_config()  # 源数据表配置

        self.data_config_watcher = QFileSystemWatcher([common_util.get_real_path('config', 'data_config.json')])
        self.data_config_watcher.fileChanged.connect(self.data_config_changed)
        self.company_config_watcher = QFileSystemWatcher([common_util.get_real_path('config', 'company_config.json')])
        self.company_config_watcher.fileChanged.connect(self.company_config_changed)

        # 初始化月份快捷选择下拉框
        self.combo_month.addItems([f'{month + 1} 月' for month in range(12)])
        self.combo_month.setToolTip(f'默认选择{datetime.now().year}年')
        self.combo_month.installEventFilter(ToolTipFilter(self.combo_month, 200, ToolTipPosition.BOTTOM))
        self.combo_month.currentTextChanged.connect(self.combo_month_changed)

        # 检查日期范围的有效性, 起始日期小于等于结束日期
        self.calendar_start.dateChanged.connect(self.date_changed)
        self.calendar_end.dateChanged.connect(self.date_changed)

        self.status_signal.connect(self.status_changed)
        self.status_signal.emit(Status.INIT)

        self.btn_import.clicked.connect(self.import_data)
        self.btn_analyse.clicked.connect(self.analyse_data)

    def analyse_data(self):
        # todo: 校验文件与模板是否匹配, 时间格式是否能正确解析
        # a 检查所有文件是否都配置了模板
        flag = True
        for file_item_widget in self.file_item_widgets:
            if not file_item_widget.combo_file_type.text():
                flag = False
                break
        if flag:
            # a.1 配置了模板的进一步检查模板是否匹配

            # b 根据模板和源数据表配置, 解析文件包含的所有 集团-公司

            self.status_signal.emit(Status.ANALYSED)
        else:
            # a.2 未配置模板的文件弹窗提示
            InfoBar.error(
                title='文件列表错误',
                content="每行必须选择一个配置!\n如无合适配置请先在源数据表配置中新增一条!",
                orient=Qt.Orientation.Horizontal,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )

    def import_data(self):
        self.status_signal.emit(Status.INIT)
        files, _ = QFileDialog.getOpenFileNames(self, '导入源数据表', r'D:\00-ZJPC\桌面\数据需求', 'Excel文件(*.xlsx)')
        if files:
            self.label_data_dir.setText('/'.join(files[0].split('/')[:-1]))
            self.data_files = [file.split('/')[-1] for file in files]

            self.list_widget_file.clear()
            for data_file in self.data_files:
                item = QListWidgetItem(self.list_widget_file)
                item_widget = FileItemView(file=data_file, data_config=self.data_config)
                self.list_widget_file.setItemWidget(item, item_widget)
                self.file_item_widgets.append(item_widget)

            self.status_signal.emit(Status.IMPORTED)

    def data_config_changed(self):
        """ 源数据表配置文件发生改变, 文件列表相应进行改变, 软件状态改变 """
        self.status_signal.emit(Status.INIT)

    def company_config_changed(self):
        if self.status != Status.INIT:
            self.status_signal.emit(Status.IMPORTED)

    def date_changed(self):
        """ 检查日期范围的有效性, 并弹出可关闭提示框 """
        if self.calendar_start.date.daysTo(self.calendar_end.date) < 0:
            if self.start_date:
                self.calendar_start.dateChanged.disconnect(self.date_changed)
                self.calendar_start.setDate(self.start_date)
                self.calendar_start.dateChanged.connect(self.date_changed)
            if self.end_date:
                self.calendar_end.dateChanged.disconnect(self.date_changed)
                self.calendar_end.setDate(self.end_date)
                self.calendar_end.dateChanged.connect(self.date_changed)
            TeachingTip.create(
                target=self.calendar_end,
                icon=InfoBarIcon.ERROR,
                title='重新选择日期',
                content="结束日期必须大于等于开始日期!",
                isClosable=True,
                tailPosition=TeachingTipTailPosition.TOP_RIGHT,
                duration=5000,
                parent=self
            )
        else:
            self.start_date = self.calendar_start.date
            self.end_date = self.calendar_end.date

    def combo_month_changed(self):
        """ 快捷选择月份下拉框触发时, 自动选择对应月份的第一天和最后一天 """
        # 快捷设置时屏蔽开始日期变化信号
        self.calendar_start.dateChanged.disconnect(self.date_changed)

        # 设置快捷选择月份的初始日期
        self.calendar_start.setDate(QDate(datetime.now().year,
                                          int(self.combo_month.text().strip(' 月')),
                                          datetime(datetime.now().year, int(self.combo_month.text().strip(' 月')), 1).day))
        # 设置快捷选择月份的结束日期
        self.calendar_end.setDate(QDate(datetime.now().year,
                                        int(self.combo_month.text().strip(' 月')),
                                        calendar.monthrange(datetime.now().year, int(self.combo_month.text().strip(' 月')))[1]))

        self.calendar_start.dateChanged.connect(self.date_changed)

    def status_changed(self, status):
        """ 根据不同阶段决定界面控件是否生效 """
        self.status = status
        if status == Status.INIT:
            self.set_status(analyse=False, export=False, clear_data_file=True, clear_data_company=True)
        if status == Status.IMPORTED:
            self.set_status(analyse=True, export=False, clear_data_file=False, clear_data_company=True)
        if status == Status.ANALYSED:
            self.set_status(analyse=True, export=True, clear_data_file=False, clear_data_company=False)
        if status == Status.MODIFIED:
            self.set_status(analyse=True, export=False, clear_data_file=True, clear_data_company=True)

    def set_status(self, analyse, export, clear_data_file, clear_data_company):
        self.btn_analyse.setEnabled(analyse)
        self.btn_export.setEnabled(export)
        self.check_box_select_all.setEnabled(not clear_data_company)
        self.line_edit_search.setEnabled(not clear_data_company)
        if clear_data_file:
            self.data_dir = ''
            self.label_data_dir.setText('')
            self.list_widget_file.clear()
            self.data_files = []
            self.data_config = common_util.load_data_config()
            self.file_item_widgets = []
        if clear_data_company:
            self.check_box_select_all.setChecked(False)
            self.list_widget_company.clear()
            self.companies = []
            self.companies_checked = []
            self.company_config = common_util.load_company_config()
