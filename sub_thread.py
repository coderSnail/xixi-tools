#!/usr/bin/python3
# -- coding: utf-8 --
#
# @Author : W9011847
# @Time : 2023/7/25 10:28
import calendar
import os.path
from datetime import datetime

from PyQt6.QtCore import QThread, pyqtSignal, QDate

from util import excel_util
from util.excel_util import load_excel


class FileCheckThread(QThread):
    file_check_signal = pyqtSignal(int, int, str, str)
    file_check_finished_signal = pyqtSignal(bool, list)  # 文件名, 是否完成, 错误信息

    def __init__(self, file_item_widgets, data_dir, data_files, data_config):
        super().__init__()
        self.file_item_widgets = file_item_widgets
        self.data_dir = data_dir
        self.data_files = data_files
        self.data_config = data_config

    def run(self) -> None:
        check_res = []
        for index, file_item in enumerate(self.file_item_widgets):
            self.file_check_signal.emit(index + 1, len(self.file_item_widgets), '检查文件', f'正在检查文件 - {self.data_files[index]}')

            file_type = file_item.combo_file_type.text()
            code, msg = excel_util.check_file_type(self.data_dir, self.data_files[index], self.data_config[file_type])
            if not code:
                check_res.append(msg)

            self.file_check_finished_signal.emit(True if index == len(self.file_item_widgets) - 1 else False, check_res)

            if index + 1 == len(self.file_item_widgets):
                self.file_check_signal.emit(index + 1, len(self.file_item_widgets), '检查文件', f'所有文件检查完成<br />')


class LoadFileThread(QThread):
    progress_signal = pyqtSignal(int, int, str, str)
    load_file_signal = pyqtSignal(dict, bool)
    msg_signal = pyqtSignal(str, str)

    def __init__(self, file_item_widgets, data_dir, data_files, data_config, company_config):
        super().__init__()
        self.file_item_widgets = file_item_widgets
        self.data_dir = data_dir
        self.data_files = data_files
        self.data_config = data_config
        self.company_config = company_config

    def run(self) -> None:
        # 反转 company_config 的 key-value
        company_group_dict = dict()
        for key in self.company_config.keys():
            for company in self.company_config[key]:
                company_group_dict[company] = key

        for index, file_item in enumerate(self.file_item_widgets):
            self.progress_signal.emit(index + 1, len(self.file_item_widgets), '分析数据', f'开始分析表格数据 - [{self.data_files[index]}]')
            excel_src = os.path.join(self.data_dir, self.data_files[index])
            file_type = file_item.combo_file_type.text()
            if not self.data_config[file_type]['has_time']:
                self.msg_signal.emit(f'请知悉: [{self.data_files[index]}] - 此文件不存在时间列, 无法指定日期范围筛选数据', '#009faa')

            title, data, title_style, data_style = load_excel(excel_src, self.data_config[file_type], company_group_dict)
            data_dict = dict()
            data_dict['file_type'] = file_type
            data_dict['channel_id'] = self.data_config[file_type]['channel_id']
            data_dict['title'] = title
            data_dict['data'] = data
            data_dict['title_style'] = title_style
            data_dict['data_style'] = data_style
            self.load_file_signal.emit(data_dict, True if index == len(self.file_item_widgets) - 1 else False)
            if index + 1 == len(self.file_item_widgets):
                self.progress_signal.emit(index + 1, len(self.file_item_widgets), '分析数据', f'所有表格数据分析完成<br />')


class LoadGroupsThread(QThread):
    generate_groups_signal = pyqtSignal(list)

    def __init__(self, start_date, end_date, excel_data_src, data_config):
        super().__init__()
        self.start_date = start_date
        self.end_date = end_date
        self.excel_data_src = excel_data_src
        self.data_config = data_config

    def run(self) -> None:
        # 集团存入set中, 自动去重
        groups_set = set()
        for key in self.excel_data_src.keys():
            # key是 oppo消耗 oppo充值 这种
            if self.data_config[key]['has_time']:
                # 有时间的表, 根据选定的日期范围进行分析
                for row_data in self.excel_data_src[key]['data']:
                    if self.start_date <= row_data[0] <= self.end_date:
                        groups_set.add(row_data[1])
            else:
                # 没有时间的表, 直接全表分析
                for row_data in self.excel_data_src[key]['data']:
                    groups_set.add(row_data[1])
        groups = list(groups_set)
        self.generate_groups_signal.emit(groups)


class ExportFileThread(QThread):
    status_signal = pyqtSignal(int)

    def __init__(self, data_dir, companies, start_date, end_date, excel_data_src):
        super().__init__()
        self.data_dir = data_dir
        self.companies = companies
        self.start_date = start_date
        self.end_date = end_date
        self.excel_data_src = excel_data_src

    def run(self) -> None:
        for index, company in enumerate(self.companies):
            self.status_signal.emit(index)
            # 每个集团公司生成一个文件
            file_name_company = company  # 文件名-集团
            file_name_channel_set = set()  # 文件名-渠道列表

            # 文件名-时间
            if isinstance(self.start_date, QDate) and isinstance(self.end_date, QDate):
                # 开始, 结束都有时间
                first_day = QDate(int(self.start_date.toString("yyyy")),
                                  int(self.start_date.toString("MM")),
                                  datetime(int(self.start_date.toString("yyyy")), int(self.start_date.toString("MM")), 1).day)
                last_day = QDate(int(self.start_date.toString("yyyy")),
                                 int(self.start_date.toString("MM")),
                                 calendar.monthrange(int(self.start_date.toString("yyyy")), int(self.start_date.toString("MM")))[1])
                if self.start_date == first_day and self.end_date == last_day:
                    file_name_time = f'{self.start_date.toString("M")}月'
                elif self.start_date.toString("yyyy") == self.end_date.toString("yyyy"):
                    file_name_time = f'{self.start_date.toString("MMdd")}-{self.end_date.toString("MMdd")}'
                else:
                    file_name_time = f'{self.start_date.toString("yyyyMMdd")}-{self.end_date.toString("yyyyMMdd")}'
            else:
                # 没有时间限制
                file_name_time = '全部'

            sheet_list = []
            for file_type in self.excel_data_src.keys():
                # 渠道拼音首字母
                file_name_channel_set.add(self.excel_data_src[file_type]['channel_id'])

                # sheet表的数据暂存到字典中
                sheet_dict = dict()
                sheet_dict['sheet_name'] = f'{file_name_time}{file_type}'
                sheet_dict['sheet_title'] = self.excel_data_src[file_type]['title']
                sheet_dict['sheet_title_style'] = self.excel_data_src[file_type]['title_style']
                sheet_dict['sheet_data_style'] = self.excel_data_src[file_type]['data_style']
                # sheet表的数据部分
                data_list = []
                for row_data in self.excel_data_src[file_type]['data']:
                    if row_data[0]:
                        # 有时间列
                        if row_data[1] == company and self.start_date <= row_data[0] <= self.end_date:
                            data_list.append(row_data[2])
                    else:
                        # 没有时间列
                        if row_data[1] == company:
                            data_list.append(row_data[2])
                sheet_dict['sheet_data_list'] = data_list

                sheet_list.append(sheet_dict)

            # 文件名
            excel_out_dir = os.path.join(self.data_dir, 'out')
            if not os.path.exists(excel_out_dir):
                os.makedirs(excel_out_dir)

            finished = excel_util.write_excel(excel_out_dir, file_name_company, file_name_channel_set, file_name_time, sheet_list)
