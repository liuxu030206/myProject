from spider.douabn100 import etree
from jiuku_download import *

real_url = 'https://www.9ku.com/playlist.php'

url = 'https://www.9ku.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def get_response(url, headers):
    """
    请求
    :param url: https://www.9ku.com/
    :param headers: headers
    :return: 响应体对象
    """
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    return response


def parse_res(response):
    """
    提取歌曲名称和转向地址
    :param response: 主url响应体对象
    :return: 歌曲名称、歌曲播放页面地址
    """
    info = []
    data = etree.HTML(response.text)
    name = data.xpath('//*[@class="topItem clearfix"]/ul/li/a[1]/@title')
    to_url = data.xpath('//*[@class="topItem clearfix"]/ul/li/a[1]/@href')
    for i in range(len(to_url)):
        info.append([name[i], url.rstrip('/') + to_url[i]])
    # 120条数据
    # print(info)
    return info


def get_data(info):
    """
    请求参数data
    :param info:
    :return:
    """
    datas = []
    for i in range(len(info)):
        num = info[i][1].split('/')[-1].split('.')[0]
        data = {'ids': f'{num}'}
        datas.append(data)
    return datas


def download(mp3_info, datas):
    for i in range(len(datas)):  # 120次
        content = post_response(real_url, headers, datas[i])
        save_mp3(mp3_info, content, i)


if __name__ == '__main__':
    mp3_info = parse_res(get_response(url, headers))
    datas = get_data(mp3_info)
    download(mp3_info, datas)
