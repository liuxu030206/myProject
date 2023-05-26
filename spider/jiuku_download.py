import requests


def post_response(url, headers, data):
    """
    :param url: 歌曲post地址
    :param headers: 请求头
    :param data: post请求数据data
    :return: 歌曲数据
    """
    response = requests.post(url, data, headers)
    return response.content


def save_mp3(mp3_info, content, i):
    """
    :param mp3_info:[歌曲名称、歌曲播放页面地址]
    :param content: 歌曲数据
    :param i: 循环控制
    :return:
    """
    with open('jiuku/' + mp3_info[i][0] + '.mp3', 'wb') as f:
        print(f"{i + 1}首：", mp3_info[i][0], "保存成功")
