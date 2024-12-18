import requests
import json
import time
import hashlib
import urllib.parse
import random
from push import push
from capture import headers, cookies, data
import os

url = "https://weread.qq.com/web/book/read"
renew_url = "https://weread.qq.com/web/login/renewal"
cookie_data = {"rq": "%2Fweb%2Fbook%2Fread"}

# 加密盐
key = "3c5c8717f3daf09iop3423zafeqoi"
num = 1


def encode_data(data, keys_to_include=None):
    sorted_keys = sorted(data.keys())
    query_string = ''

    for key in sorted_keys:
        if keys_to_include is None or key in keys_to_include:
            value = data[key]
            encoded_value = urllib.parse.quote(str(value), safe='')
            query_string += f'{key}={encoded_value}&'

    if query_string.endswith('&'):
        query_string = query_string[:-1]

    return query_string


def cal_hash(input_string):
    _7032f5 = 0x15051505
    _cc1055 = _7032f5
    length = len(input_string)
    _19094e = length - 1

    while _19094e > 0:
        _7032f5 = 0x7fffffff & (_7032f5 ^ ord(input_string[_19094e]) << (length - _19094e) % 30)
        _cc1055 = 0x7fffffff & (_cc1055 ^ ord(input_string[_19094e - 1]) << _19094e % 30)
        _19094e -= 2

    return hex(_7032f5 + _cc1055)[2:].lower()


def get_wr_skey():
    data = json.dumps(cookie_data, separators=(',', ':'))
    response = requests.post(renew_url, headers=headers, cookies=cookies, data=data)
    # print(response.text)
    cookie_str = response.headers['Set-Cookie']
    # print(cookie_str)
    for cookie in cookie_str.split(';'):
        if cookie.__contains__("wr_skey"):
            wr_skey = cookie[-8:]
            print(f"数据初始化成功！当前密钥值为{wr_skey}!")
            cookies['wr_skey'] = wr_skey
            return wr_skey


while True:
    # 处理数据（后端只需要ct字段和s字段正确即可）
    print(f"-------------------第{num}次，共阅读{num * 0.5}分钟-------------------")
    data['ct'] = int(time.time())
    data['ts'] = int(time.time() * 1000)
    data['rn'] = random.randint(0, 1000)  # 1000以内的随机整数值
    data['sg'] = hashlib.sha256(("" + str(data['ts']) + str(data['rn']) + key).encode()).hexdigest()
    print(f"sg:{data['sg']}")
    data['s'] = cal_hash(encode_data(data))
    print(f"s:{data['s']}")

    sendData = json.dumps(data, separators=(',', ':'))
    response = requests.post(url, headers=headers, cookies=cookies, data=sendData)
    resData = response.json()
    print(response.json())

    if 'succ' in resData:
        print("数据格式正确，阅读进度有效！")
        num += 1
        time.sleep(30)
    else:
        print("数据格式问题,尝试初始化cookie值")
        cookies['wr_skey'] = get_wr_skey()
        num -= 1

    PUSHPLUS_TOKEN = os.getenv("PUSHPLUS_TOKEN")
    # 每一次代表30秒，比如你想刷1个小时这里填120，你只需要签到这里填2次
    if num == 120:
        print("阅读脚本运行已完成！")
        push("阅读脚本运行已完成！", method="pushplus", pushplus_token=PUSHPLUS_TOKEN)
        break
    # 确认无s字段
    data.pop('s')
