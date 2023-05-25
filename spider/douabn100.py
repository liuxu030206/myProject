import csv
import re

import lxml.html

etree = lxml.html.etree

import parsel
import requests

url = 'https://movie.douban.com/chart'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def get_data(url, headers, *args):
    response = requests.get(url=url, headers=headers)
    return response.text


def parse_data(data):
    info = []
    se = parsel.Selector(data)
    title = se.css('.nbg::attr(title)').getall()
    inf = se.css('td > div > p::text').getall()
    for i in range(len(title)):
        info.append([title[i], inf[i]])
    return info


def parse_data_2(data):
    html = etree.HTML(data)
    title = html.xpath('//td/div/a/text()')
    inf = html.xpath('//td//div//p/text()')
    info = []
    for i in range(0, len(title), 2):
        info.append(
            title[i].replace('\n                        ', '').replace('\n                        / ', '').replace('/',
                                                                                                                   ''))
    # print(info)
    return info


def save_data(info_list):
    with open('top10.csv', mode='w', encoding='utf8', newline='') as f:
        w = csv.writer(f, delimiter=',')
        w.writerow(['电影名', '电影信息'])
        for i in range(len(info_list)):
            w.writerow(info_list[i])


if __name__ == '__main__':
    save_data(parse_data(get_data(url, headers)))
    save_data(parse_data_2(get_data(url, headers)))
