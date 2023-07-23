from enum import Enum


class Status(Enum):
    INIT = 1  # 初始状态
    IMPORTED = 2  # 已导入源数据表
    ANALYSED = 3  # 分析完成
    MODIFIED = 4  # 文件的模板发生修改
