import csv
import json
import time

import requests

url = 'https://data.stats.gov.cn/search.htm?'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'wzws_sessionid=oGRvI5aBYzJlODc3gDExNy4xNzYuMTg1LjgxgmZjNWVlMQ==; JSESSIONID=r49SIoZOyNDtawS-6uwFfTTJTvMHaONsL_kAPsO3glr_HfvA-Wtv!-1876458310; u=2; experience=show; wzws_cid=41fe6dfc1a8651432063c8f183966b7466ce4077bee9b5c5a620ce4d12b8babe1adc7fea19783a233b4fdc36a6ec43aeb01580aeb422f019fc231f959b16dc45f307c15f71965ccbba377f4fe605a65e9d0975e48c19b4d88d00afc5e49dcb6d',
    'Host': 'data.stats.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',

}


# 构建请求参数
def page(i, year):
    params = {
        's': f'{year}年可支配工资',
        'm': 'searchdata',
        'db': '',
        'p': i
    }
    return params


# 获取数据
def get_data(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params, verify=False)
    response.encoding = response.apparent_encoding
    return json.loads(response.text)


# 提取数据
def parse_data(json_data):
    info = []
    for i in range(10):
        data = json_data['result'][i]['data']
        date_ = json_data['result'][i]['sj']
        info.append([date_, data])
    return info


# 保存数据
def save_data(info_list, y):
    with open('D:\\桌面\\Python\\myProject\\csv_file\\salary.csv', mode='a+', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter=',')
        for i in range(len(info_list)):
            # 空值处理
            if info_list[i][1] == '':
                info_list[i][1] = 0
            w.writerow([y, info_list[i][0], info_list[i][1]])
            print(y, info_list[i][0], info_list[i][1])


def run():
    for y in range(2013, 2021):
        for i in range(93):
            save_data(parse_data(get_data(url, headers, page(i, y))), y)
            time.sleep(1)


if __name__ == '__main__':
    run()
