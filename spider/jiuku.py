import requests

from spider.douabn100 import etree

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
    return info


def get_data(info):
    """
    请求参数data
    :param info:
    :return:
    """
    datas = []
    for item in info:
        num = item[1].split('/')[-1].split('.')[0]
        data = {'ids': f'{num}'}
        datas.append(data)
    return datas


def p(datas):
    """
    音乐下载链接地址
    :param datas:
    :return:
    """
    datas = get_data(parse_res(get_response(url, headers)))
    mp3_list = []
    for i in range(len(datas)):
        response = requests.post(url=real_url, data=datas[i], headers=headers)
        mp3_list.append(response.json()[0]['wma'])
        print(response.json()[0]['wma'])
    return mp3_list


def save_mp3(mp3_info, mp3_list):
    """
    :param list: [歌曲名称、歌曲播放页面地址]
    :return:
    """
    for i in range(len(mp3_info)):
        mp_download = get_response(mp3_list[i], headers).content
        with open('jiuku' + mp3_info[i][0] + '.mp3', 'wb') as f:
            f.write(mp_download)
            print(mp3_info[i][0], "保存成功")


if __name__ == '__main__':
    mp3_info = parse_res(get_response(url, headers))
    datas = get_data(mp3_info)
    mp3_list = p(datas)
    save_mp3(mp3_info, mp3_list)
