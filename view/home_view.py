import calendar
from datetime import datetime
from enum import Enum

from PyQt6.QtCore import QDate, pyqtSignal, QFileSystemWatcher, Qt
from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QWidget, QFileDialog, QListWidgetItem, QCompleter
from qfluentwidgets import ToolTipFilter, ToolTipPosition, TeachingTip, InfoBarIcon, TeachingTipTailPosition, InfoBar, InfoBarPosition, CheckBox

from sub_thread import FileCheckThread, LoadFileThread, LoadGroupsThread, ExportFileThread
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

        self.excel_data_src = dict()  # 导入时的原始数据

        self.data_dir = ''  # 源数据表文件路径
        self.data_files = []  # 源数据表
        self.data_config = common_util.load_data_config()  # 源数据表配置
        self.file_item_widgets = []  # 文件列表行控件

        self.companies_checked = []  # 选中的集团名
        self.companies = []  # 分析后所有源数据表存在的集团名(公司映射后的)
        self.company_config = common_util.load_company_config()  # 集团公司配置

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
        self.btn_export.clicked.connect(self.export_data)

    def export_status(self, exported_index):
        self.set_progress_bar(exported_index + 1, len(self.companies_checked), '正在导出', f'正在导出数据 - [{self.companies_checked[exported_index].text()}]')
        if exported_index + 1 == len(self.companies_checked):
            self.set_progress_bar(exported_index + 1, len(self.companies_checked), '导出完成', f'已导出选中集团的全部数据<br />')
            self.status_signal.emit(self.status.EXPORTED)

    def export_data(self):
        """ 导出选中的数据 """
        self.status_signal.emit(self.status.EXPORTING)
        if (self.calendar_start.date.isNull() and self.calendar_end.date.isNull()) or (not self.calendar_start.date.isNull() and not self.calendar_end.date.isNull()):

            if self.companies_checked:
                self.export_file_thread = ExportFileThread(self.data_dir, [company.text() for company in self.companies_checked], self.start_date, self.end_date, self.excel_data_src)
                self.export_file_thread.status_signal.connect(self.export_status)
                self.export_file_thread.start()
            else:
                InfoBar.error(
                    title='文件导出错误',
                    content="没有选择任何公司集团啊!\n你想做甚?!嗯~???",
                    orient=Qt.Orientation.Vertical,
                    position=InfoBarPosition.TOP,
                    duration=3000,
                    parent=self
                )
        else:
            InfoBar.error(
                title='文件导出错误',
                content="既然选择了时间, 为啥空一个不选呢???\n开始和结束时间都要选上喔~",
                orient=Qt.Orientation.Vertical,
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )

    def analyse_data(self):
        self.status_signal.emit(self.status.IMPORTED)
        self.btn_analyse.setEnabled(False)
        # a 检查所有文件是否都配置了模板
        flag = True
        for file_item_widget in self.file_item_widgets:
            if not file_item_widget.combo_file_type.text():
                flag = False
                break
        if not flag:
            # a.1 未配置模板的文件弹窗提示
            InfoBar.error(
                title='文件列表错误',
                content="每行必须选择一个配置!\n如无合适配置请先在源数据表配置中新增一条!",
                orient=Qt.Orientation.Vertical,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            self.status_signal.emit(Status.IMPORTED)
        elif len([file_item_widget.combo_file_type.currentText() for file_item_widget in self.file_item_widgets]) != len(
                set([file_item_widget.combo_file_type.currentText() for file_item_widget in self.file_item_widgets])):
            InfoBar.error(
                title='文件列表错误',
                content="多个文件选择了相同配置,这不合理!\n可能是识别错误,请手动选择或修改源数据表配置!",
                orient=Qt.Orientation.Vertical,
                isClosable=False,  # disable close button
                position=InfoBarPosition.TOP,
                duration=3000,
                parent=self
            )
            self.status_signal.emit(Status.IMPORTED)
        else:
            # a.2 进一步检查文件与模板是否匹配
            self.file_check_thread = FileCheckThread(self.file_item_widgets, self.data_dir, self.data_files, self.data_config)
            self.file_check_thread.file_check_signal.connect(self.set_progress_bar)
            self.file_check_thread.file_check_finished_signal.connect(self.file_check_finished)
            self.file_check_thread.start()

    def file_check_finished(self, is_finished, check_res):

        if is_finished:
            if check_res:
                check_res = '\n'.join(check_res)
                self.log('文件模板匹配错误, 请根据提示重新设置文件对应模板', 'red')
                InfoBar.error(
                    title='文件列表错误',
                    content=f"模板匹配失败:\n{check_res}",
                    orient=Qt.Orientation.Vertical,
                    isClosable=True,  # disable close button
                    position=InfoBarPosition.TOP,
                    duration=10000,
                    parent=self
                )
                self.status_signal.emit(Status.IMPORTED)
            else:
                # b 根据模板和源数据表配置, 解析文件包含的所有 集团-公司
                self.load_file_thread = LoadFileThread(self.file_item_widgets, self.data_dir, self.data_files, self.data_config, self.company_config)
                self.load_file_thread.load_file_signal.connect(self.file_loaded)
                self.load_file_thread.progress_signal.connect(self.set_progress_bar)
                self.load_file_thread.msg_signal.connect(self.log)
                self.load_file_thread.start()

    def file_loaded(self, data_dict, is_finished):
        # 处理载入的数据(以源数据表配置名为key, 保存)
        self.excel_data_src[data_dict['file_type']] = data_dict
        if is_finished:
            # 处理开始时间和结束时间
            self.start_date = datetime.strptime("1970-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
            self.end_date = datetime.now()
            if self.calendar_start.date:
                self.start_date = self.calendar_start.date
            if self.calendar_end.date:
                self.end_date = self.calendar_end.date

            self.load_groups_thread = LoadGroupsThread(self.start_date, self.end_date, self.excel_data_src, self.data_config)
            self.load_groups_thread.generate_groups_signal.connect(self.init_company_list_and_company_search)
            self.load_groups_thread.start()

    def init_company_list_and_company_search(self, groups):
        # 集团列表和搜索框填充数据
        self.groups = groups
        self.list_widget_company.clear()
        self.line_edit_search.clear()
        self.company_check_box_list = []  # 集团列表

        # 搜索框赋值
        self.completer = QCompleter(self.groups, self.line_edit_search)
        self.completer.setFilterMode(Qt.MatchFlag.MatchContains)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.line_edit_search.setCompleter(self.completer)
        self.line_edit_search.textChanged.connect(self.search_group_checked)
        self.check_box_select_all.toggled.connect(self.check_all_company)

        # 集团列表赋值
        self.label_total_count.setText(f'{len(self.groups)}')
        for group in self.groups:
            check_box = CheckBox()
            check_box.setObjectName(f"check_box_{group}")
            check_box.setText(group)
            self.company_check_box_list.append(check_box)
            check_box.toggled.connect(self.verify_check_all)

            item = QListWidgetItem(self.list_widget_company)
            item.setToolTip(group)
            self.list_widget_company.setItemWidget(item, check_box)
        self.status_signal.emit(Status.ANALYSED)

    def search_group_checked(self):
        if self.groups.__contains__(self.line_edit_search.text()):
            check_box = self.findChild(CheckBox, f'check_box_{self.line_edit_search.text()}')
            check_box.setChecked(True)
            check_box.setFocus()
            self.line_edit_search.setText('')

    def check_all_company(self):
        self.companies_checked = []
        for group in self.groups:
            check_box = self.findChild(CheckBox, f'check_box_{group}')
            check_box.toggled.disconnect(self.verify_check_all)
            check_box.setChecked(self.check_box_select_all.isChecked())
            check_box.toggled.connect(self.verify_check_all)
            if self.check_box_select_all.isChecked():
                self.companies_checked.append(check_box)
        self.label_checked_count.setText(f'{len(self.companies_checked)}')

    def verify_check_all(self):
        flag = True
        self.companies_checked = []
        for group in self.groups:
            check_box = self.findChild(CheckBox, f'check_box_{group}')
            if check_box.isChecked():
                self.companies_checked.append(check_box)
            flag = flag and check_box.isChecked()
        self.label_checked_count.setText(f'{len(self.companies_checked)}')

        if self.check_box_select_all.isChecked():
            self.check_box_select_all.toggled.disconnect(self.check_all_company)
            self.check_box_select_all.setChecked(flag)
            self.check_box_select_all.toggled.connect(self.check_all_company)
        else:
            self.check_box_select_all.setChecked(flag)

    def import_data(self):
        self.status_signal.emit(Status.INIT)
        files, _ = QFileDialog.getOpenFileNames(self, '导入源数据表', '', 'Excel文件(*.xlsx)')
        if files:
            self.log('导入源数据表, 自动匹配模板')
            self.data_dir = '/'.join(files[0].split('/')[:-1])
            self.label_data_dir.setText(self.data_dir)
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
            if self.data_files:
                self.status_signal.emit(Status.IMPORTED)

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
                                        calendar.monthrange(datetime.now().year,
                                                            int(self.combo_month.text().strip(' 月')))[1]))

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
        if status == Status.EXPORTING:
            self.set_status(analyse=False, export=False, clear_data_file=False, clear_data_company=False)
        if status == Status.EXPORTED:
            self.set_status(analyse=True, export=True, clear_data_file=False, clear_data_company=False)

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
            self.excel_data_src = dict()
            self.label_total_count.setText('0')
            self.label_checked_count.setText('0')

    def log(self, log_text, color=None):
        if color:
            self.text_log.insertHtml(f'<font color="{color}">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:  {log_text}</font><br />')
        else:
            self.text_log.insertHtml(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}:  {log_text}<br />')
        self.text_log.moveCursor(QTextCursor.MoveOperation.End)

    def set_progress_bar(self, current, total, msg, log):
        self.process_bar.setMaximum(total)
        self.process_bar.setVal(current)
        self.label_process_total.setText(str(total))
        self.label_process_current.setText(str(current))
        self.label_msg.setText(msg)
        self.log(log)
