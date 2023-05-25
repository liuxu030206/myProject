import csv
import re

import lxml.html

etree = lxml.html.etree

import parsel
import requests

url = 'https://www.gaokao.com/sichuan/scgkcj/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def get_data(url, headers, *args):
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    return response.text


def parse_data(data):
    info = []
    se = parsel.Selector(data)
    w_yiben = se.css('.c_blue > .first::text').get()
    w_erben = se.css('.c_white > .first::text').get()
    year = se.css(' .wkTit > th::text').getall()[:11]
    first_ = se.css(' .c_blue > td::text').getall()

    w_first = first_[1:12]
    second_ = se.css('.c_white > td::text').getall()
    w_second = second_[1:12]

    for i in range(len(w_first)):
        info.append((year[i], w_yiben, w_first[i]))
        info.append((year[i], w_erben, w_second[i]))
    return info


def parse_data_2(data):
    html = etree.HTML(data)
    info = []
    a=[]
    w_yiben = html.xpath('//tr[@class="c_blue"]/td[@class="first"]/text()')[0]
    w_year = html.xpath('//tr[@class="wkTit"]/th/text()')[:11]
    w_erben = html.xpath('//tr[@class="c_white"]/td[1]/text()')[0]
    first_ = html.xpath('//tr[@class="c_blue"]/td/text()')[1:12]
    second_ = html.xpath('//tr[@class="c_white"]/td/text()')[1:12]

    for i in range(len(first_)):
        info.append((w_year[i], w_yiben, first_[i]))
        info.append((w_year[i], w_erben, second_[i]))
    return info


def save_data(info_list):
    with open('历年文科.csv', mode='w', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['年份', '类别', '分数'])
        for i in range(len(info_list)):
            w.writerow(info_list[i])


if __name__ == '__main__':
    # xpath
    print(parse_data_2(get_data(url, headers)))
    # css
    print(parse_data(get_data(url, headers)))
    # 保存数据
    save_data(parse_data(get_data(url, headers)))
