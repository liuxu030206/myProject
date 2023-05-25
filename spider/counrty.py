import csv
import json

import requests

url = 'https://data.stats.gov.cn/search.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def page(i):
    params = {
        's': '2000年-2010年gdp',
        'm': 'searchdata',
        'db': '',
        'p': i
    }
    return params


def get_data(url, headers, params):
    response = requests.get(url=url, headers=headers, params=params, verify=False)
    return json.loads(response.text)


def parse_data(json_data):
    info = []
    for i in range(10):
        name = json_data['result'][i]['zb']
        reg = json_data['result'][i]['reg']
        data = json_data['result'][i]['data']
        date_ = json_data['result'][i]['sj']
        db = json_data['result'][i]['db']
        info.append([name, reg, data, date_, db])
    return info


def save_data(info_list):
    with open('govn.csv', mode='w', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['指标', '地区', '数值', '时间', '所属栏目'])
        for i in range(len(info_list)):
            w.writerow(info_list[i])
            print(info_list[i])


if __name__ == '__main__':
    for i in range(2000):
        save_data(parse_data(get_data(url, headers, page(i))))
