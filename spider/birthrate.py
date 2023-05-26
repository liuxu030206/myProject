import csv

import re

import requests

url = 'https://data.stats.gov.cn/search.htm?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def page(i):
    params = {
        's': '2017-2019年云南、四川、重庆的人口出生率',
        'm': 'searchdata',
        'db': '',
        'p': i
    }
    return params


def get_data(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params, verify=False)
    response.encoding = response.apparent_encoding
    return response.text


def parse_data(data):
    info = []
    data_ = re.findall('data":"(.*?)","', data, re.S)
    db = re.findall('db":"(.*?)","exp', data, re.S)
    rank = re.findall('"rank":(.*?),"reg', data, re.S)
    reg = re.findall('reg":"(.*?)","report', data, re.S)
    sj = re.findall('sj":"(.*?)","zb', data, re.S)
    zb = re.findall('zb":"(.*?)"}', data, re.S)
    for i in range(len(zb)):
        info.append([data_[i], db[i], rank[i], reg[i], sj[i], zb[i]])
    return info


def save_data(info_list):
    with open('../csv_file/birthrate.csv', mode='a', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter=',')
        # w.writerow(['数值', '所属栏目', '排名', '地区', '时间', '指标'])
        for i in range(len(info_list)):
            w.writerow(info_list[i])
            print(info_list[i])


if __name__ == '__main__':
    # print(get_data(url, headers, page(0)))
    for i in range(200):
        save_data(parse_data(get_data(url, headers, page(i))))
