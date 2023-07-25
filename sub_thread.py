#!/usr/bin/python3
# -- coding: utf-8 --
#
# @Author : W9011847
# @Time : 2023/7/25 10:28
from PyQt6.QtCore import QThread, pyqtSignal

from util import excel_util
from util.excel_util import load_excel


class FileCheckThread(QThread):
    file_check_signal = pyqtSignal(str)
    file_check_finished_signal = pyqtSignal(str, bool, list)  # 文件名, 是否完成, 错误信息

    def __init__(self, file_item_widgets, data_dir, data_files, data_config):
        super().__init__()
        self.file_item_widgets = file_item_widgets
        self.data_dir = data_dir
        self.data_files = data_files
        self.data_config = data_config

    def run(self) -> None:
        check_res = []
        # todo 这里循环似乎不正确
        for index, file_item in enumerate(self.file_item_widgets):
            self.file_check_signal.emit(self.data_files[index])

            file_type = file_item.combo_file_type.text()
            code, msg = excel_util.check_file_type(self.data_dir, self.data_files[index], self.data_config[file_type])
            if not code:
                check_res.append(msg)

            self.file_check_finished_signal.emit(self.data_files[index], True if index == len(self.file_item_widgets) - 1 else False, check_res)


class LoadFileThread(QThread):
    load_file_signal = pyqtSignal(dict)

    def __init__(self, excel_src, data_config):
        super().__init__()
        self.excel_src = excel_src
        self.data_config = data_config

    def run(self) -> None:
        print(self.excel_src)
        title, data, style = load_excel(self.excel_src, self.data_config)
        data_dict = dict()
        data_dict['title'] = title
        data_dict['data'] = data
        data_dict['style'] = style
        self.load_file_signal.emit(data_dict)
