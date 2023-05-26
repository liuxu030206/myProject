import pandas as pd


def x():
    df = pd.read_csv('../csv_file/test.csv')
    # print(df)

    # 查询 2013年的所有值
    data = df.groupby('year')
    print(data.get_group(2013))


if __name__ == '__main__':
    x()
