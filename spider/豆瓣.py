import csv

import requests

url = 'https://movie.douban.com/j/chart/top_list?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

param = {
    'type_name': '动作',
    'type': 5,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20
}

def get_data(url, headers,param):
    response = requests.get(url=url, headers=headers, params=param)
    json_data = response.json()
    return json_data


def save_data(json_data):
    with open('movie.csv', mode='w', encoding='utf-8', newline='') as f:
        wr = csv.writer(f, delimiter=',')
        wr.writerow(['电影名', '上映时间', '类型', '链接地址', '地区', '演员', '评分', '评价人数'])
        for i in range(len(json_data)):
            name = json_data[i]['title']
            release_date = json_data[i]['release_date']
            url_ = json_data[i]['url']
            regions = json_data[i]['regions']
            types_ = json_data[i]['types']
            actors = json_data[i]['actors']
            score = json_data[i]['score']
            vote_count = json_data[i]['vote_count']
            wr.writerow([name, release_date, types_, url_, regions, actors, score, vote_count])
            print(name, url_, regions, types_, actors)


if __name__ == '__main__':
    js = get_data(url,headers, param)
    save_data(js)