import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def read():
    df = pd.read_csv('../csv_file/test.csv')
    # print(df)
    return df


def group(df):
    data = df.groupby('year')
    # print(data.get_group(2013))
    for i in range(2013, 2021):
        ydf = data.get_group(i)
        # print(ydf)
        remodel(ydf)


def remodel(df):
    # 计算每季度真实可支配工资
    da = df['data'].diff().abs()
    data2 = list(da)
    data2 = data2[1:]
    data2.append(round(list(df['data'])[-1]))
    # print(data2)
    df['data'] = data2
    # 计算相对增长率
    dt = df['data'].pct_change()
    data = list(round(dt * 100))
    for i in range(len(data)):
        if i == 0:
            data[i] = 0
        data[i] = str(data[i]) + "%"
    df.loc[:, 'raise_rate'] = data
    print(df)


if __name__ == '__main__':
    group(read())
