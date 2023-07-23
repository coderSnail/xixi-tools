from datetime import datetime

from openpyxl import load_workbook


def load_excel(excel, _sheet_name, _channel, _type, _date_col, _date_format, _name_col_list):
    # 0 - 渠道名, 1 - 类型(消耗/充值)
    result = [_channel, _type]

    work_book = load_workbook(excel)
    sheet = work_book[_sheet_name]
    rows = list(sheet.iter_rows(values_only=True))
    # 2 - 表头
    result.append(rows[0])

    temp = []
    for row in rows[1:]:
        # 3.1 - 日期
        new_row = [datetime.strptime(row[rows[0].index(_date_col)], _date_format)]
        # 3.2 - 客户名
        name_list = []
        for col in _name_col_list:
            name_list.append(row[rows[0].index(col)].split('-')[0])
        new_row.append(name_list)
        # 3.3 - 每行数据
        new_row.append(row)
        # 数据汇总成二维数组
        temp.append(new_row)

    # 3 - 数据
    result.append(temp)
    print(result[0], result[1], result[2])
    return result
