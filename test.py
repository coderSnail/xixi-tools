from util.common_util import get_real_path
from util.excel_util import load_excel

# oppo_recharge = load_excel(r'D:\00-ZJPC\桌面\数据需求\OPPO6月转账记录.xlsx', '账务流水', 'oppo', '充值', '时间', '%Y-%m-%d %H:%M:%S', ['客户名称'])
# oppo_cost = load_excel(r'D:\00-ZJPC\桌面\数据需求\OPPO6月消耗.xlsx', '代理商消耗报表', 'oppo', '消耗', '时间', '%Y%m%d', ['客户名称'])
# vivo_recharge = load_excel(r'D:\00-ZJPC\桌面\数据需求\vivo6月转账记录.xlsx', 'sheet', 'vivo', '充值', '转账时间', '%Y-%m-%d %H:%M:%S', ['转出方公司名', '转入方公司名'])
# huawei_recharge = load_excel(r'D:\00-ZJPC\桌面\数据需求\华为商店充值数据月表.xlsx', '明细数据', 'huawei', '充值', '转账时间', '%Y-%m-%d', ['客户名称'])
#
# print(len([item for item in oppo_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
# print(len([item for item in oppo_cost[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
# print(len([item for item in vivo_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
# print(len([item for item in huawei_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))


if __name__ == '__main__':
    print(get_real_path('ui', 'config.ui'))
