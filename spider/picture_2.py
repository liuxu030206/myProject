import re

import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def page():
    url_list = []
    for i in range(100):
        url = f'https://sc.chinaz.com/tupian/index_{i + 1}.html'
        # https://sc.chinaz.com/tupian/index_3.html
        # print(url)
        url_list.append(url)
    return url_list


def get_url(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    # print(response.url)
    return response


def parse_url(response):
    info = []
    # print(response.text)
    name = re.findall('<a class=".*" href=".*title=".*" target="_blank">(.*?)</a>', response.text, re.S)
    pic_url = re.findall('data-original="(.*?)"', response.text, re.S)
    for i in range(len(name)):
        # print(name[i], "https:" + pic_url[i])
        info.append([name[i], "https:" + pic_url[i]])
    return info


def save_image(list):
    for i in range(len(list)):
        pic_res = get_url(list[i][1], headers)
        with open("pic_2/" + list[i][0] + ".png", mode='wb') as f:
            f.write(pic_res.content)
            print(list[i][0] + ".png 保存成功")


if __name__ == '__main__':
    for p in page():
        # print(p)
        info = parse_url(get_url(p, headers))
        save_image(info)
