import pandas as pd

data = [
    ('2013', '第四季度', 10411),
    ('2013', '第三季度', 7834),
    ('2013', '第二季度', 5225),
    ('2013', '第一季度', 2849)
]


def p(data):
    df = pd.DataFrame(data, columns=['year', 'month', 'value'])
    print(df)
    print("------------------------------------------------")
    data = df['value'].pct_change()
    print(data)
    # 把统计结果转化为列表
    data = list(round(data * 100))
    for i in range(len(data)):
        if i == 0:
            data[i] = 0
        data[i] = str(data[i]) + "%"
    # print(data)
    print("-----------------------------------------------")
    # 将处理后的增长率添加到数据帧中
    df['raise_rate'] = data
    print(df)


if __name__ == '__main__':
    p(data)
