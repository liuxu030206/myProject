import requests
from lxml import etree

url_ = 'http://pic.netbian.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def page():
    url_list = []
    for i in range(25):
        url = f'http://pic.netbian.com/4kqiche/index_{i + 1}.html'
        url_list.append(url)
    return url_list


def get_url(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    return response


def parse_url(text):
    info = []
    html = etree.HTML(text.text)
    name = html.xpath('//ul[@class="clearfix"]/li/a/b/text()')
    pic_url = html.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    for i in range(len(name)):
        # print(name[i], url.rstrip('/').replace('4kqiche', '') + pic_url[i])
        info.append([name[i], url_ + pic_url[i]])
    return info


def save_image(list):
    for i in range(len(list)):
        pic_res = get_url(list[i][1], headers)
        with open("pic/" + list[i][0] + ".png", mode='wb') as f:
            f.write(pic_res.content)
            print(list[i][0] + ".png 保存成功")


if __name__ == '__main__':
    for p in page():
        print(p)
        info = parse_url(get_url(p, headers))
        save_image(info)
