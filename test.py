from util.common_util import get_real_path, load_data_config
from util.excel_util import load_excel

base_dir = r'D:\00-ZJPC\桌面\数据需求'
# oppo_recharge = load_excel(rf'{base_dir}\OPPO6月转账记录.xlsx', '账务流水', 'oppo', '充值', '时间', '%Y-%m-%d %H:%M:%S', ['客户名称'])
# oppo_cost = load_excel(rf'{base_dir}\OPPO6月消耗.xlsx', load_data_config()['oppo消耗'])
# vivo_recharge = load_excel(rf'{base_dir}\vivo6月转账记录.xlsx', load_data_config()['vivo充值'])
vivo_recharge = load_excel(rf'{base_dir}\vivo6月转账记录.xlsx', load_data_config()['vivo充值'])
# huawei_recharge = load_excel(rf'{base_dir}\华为商店充值数据月表.xlsx', load_data_config()['华为充值'])
#
# print(len([item for item in oppo_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
# print(len([item for item in oppo_cost[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
# print(len([item for item in vivo_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))
print(vivo_recharge[0])
print(len(vivo_recharge[1]))
for item in vivo_recharge[1]:
    if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司'):
        print(item)

print(vivo_recharge[2])
# print(len([item for item in huawei_recharge[3] if item[1].__contains__('广州联动网络科技有限公司') or item[1].__contains__('霍尔果斯兰图网络科技有限公司')]))