import os
from datetime import datetime

from openpyxl import load_workbook


def load_excel(excel, data_config, company_group_dict):
    # 1. 加载 excel 文件
    work_book = load_workbook(excel)
    sheet = work_book[data_config['sheet']]
    rows = list(sheet.iter_rows(values_only=True))
    # 2 - 表头
    if data_config['special_type'] == '指定列':
        data_title = [col for index, col in enumerate(rows[0]) if data_config['special_col'].__contains__(get_char(index))]
    elif data_config['special_type'] == '排除列':
        data_title = [col for index, col in enumerate(rows[0]) if not data_config['special_col'].__contains__(get_char(index))]
    else:
        data_title = list(rows[0])
    # 3. 表格数据
    data = []
    for row in rows[1:]:
        # 3.1 - 日期
        if data_config['has_time']:
            data_row = [datetime.strptime(row[rows[0].index(data_config['time_col'])], data_config['time_format'])]
        else:
            data_row = [None]
        # 3.2 - 客户名
        group_name = ''
        for col in data_config['customer_col']:
            company = row[rows[0].index(col)].split('-')[0]
            # todo 本公司主体, 排除掉
            if company != '欢聚时代文化传媒（北京）有限公司':
                group_name = company
                if company_group_dict.keys().__contains__(company):
                    group_name = company_group_dict[company]

        data_row.append(group_name)
        # 3.3 - 每行数据
        if data_config['special_type'] == '指定列':
            data_row.append([col for index, col in enumerate(row) if data_config['special_col'].__contains__(get_char(index))])
        elif data_config['special_type'] == '排除列':
            data_row.append([col for index, col in enumerate(row) if not data_config['special_col'].__contains__(get_char(index))])
        else:
            data_row.append(list(row))

        # 数据汇总成二维数组
        data.append(data_row)

    # todo 4. 标题样式和数据样式
    title_style = []
    data_style = []

    return data_title, data, title_style, data_style


def get_index(capital):
    """
    大写字母（Excel列头）转索引
    :param capital: 'A' --> 0, 'AA' --> 26
    :return: int
    """
    number = 0
    capital = capital.upper()
    for char in capital:
        number = number * 26 + ord(char) - ord('A') + 1
    return number - 1


def get_char(number):
    """
    索引转大写字母（Excel列头）
    :param number: 0 --> 'A', 26 --> 'AA'
    :return: str
    """
    factor, moder = divmod(number, 26)
    mod_char = chr(moder + 65)
    if factor:
        mod_char = get_char(factor - 1) + mod_char
    return mod_char


def check_file_type(data_dir, file, config):
    # 初步检查模板是否匹配文件, 主要是列字段对应和时间格式
    excel_file = os.path.join(data_dir, file)
    work_book = load_workbook(excel_file)
    # sheet 名称检查
    try:
        sheet = work_book[config['sheet']]
    except Exception:
        return False, f'[{file}] sheet表名配置错误'
    rows = list(sheet.iter_rows(values_only=True, max_row=2))
    # 字段检查
    if config['has_time'] and not rows[0].__contains__(config['time_col']):
        return False, f'[{file}] 不存在时间列/时间列字段名配置错误'
    for customer_col in config['customer_col']:
        if not rows[0].__contains__(customer_col):
            return False, f'[{file}] 客户名配置错误'
    # 时间格式检查
    if config['has_time']:
        try:
            datetime.strptime(rows[1][rows[0].index(config['time_col'])], config['time_format'])
        except Exception:
            return False, f'[{file}] 时间格式配置错误'

    return True, ''