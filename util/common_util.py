from datetime import datetime
import json
import os


def get_real_path(*relative_path):
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), *relative_path)


def get_time():
    return str(datetime.timestamp(datetime.now())).replace('.', '')


def load_data_config():
    with open(get_real_path('config', 'data_config.json'), mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def save_data_config(data_config):
    with open(get_real_path('config', 'data_config.json'), mode='w', encoding='utf-8') as f:
        f.write(json.dumps(data_config))


def load_company_config():
    with open(get_real_path('config', 'company_config.json'), mode='r', encoding='utf-8') as f:
        return json.loads(f.read())


def save_company_config(company_config):
    with open(get_real_path('config', 'company_config.json'), mode='w', encoding='utf-8') as f:
        f.write(json.dumps(company_config))


if __name__ == '__main__':
    print(get_time())
