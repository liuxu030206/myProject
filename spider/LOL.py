import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


def get_data(url, headers, *args):
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    return response.json()


def parse_data(data):
    print(len(data))
    for i in range(len(data)):
        print(data[i]['cname'])


if __name__ == '__main__':
    parse_data(get_data(url, headers))
