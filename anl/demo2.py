import openpyxl as xl
import pandas as pd


def one():
    data = [("张三", 18), ("李四", 19), ("王五", 20)]
    df = pd.DataFrame(data, columns=['name', 'age'], index=[1, 2, 3])
    # 存入excel
    df.to_excel('../csv_file/test.xlsx')
    print("写入完毕")


def two():
    data = pd.read_excel('../csv_file/test.xlsx')
    print(data)


def three():
    data = [("张三", 18, 100), ("李四", 19, 60), ("王五", 20, 87)]
    df = pd.DataFrame(data, columns=['name', 'age', 'score'])
    print(df)
    data = df.sum()  # 含有数字的列全部计算
    # print(data)

    data1 = df['age'].sum()  # 单独一列的数字求和
    # print(data1)

    data2 = df['score'].mean()  # 求当前列的平均值
    # print(round(data2, 1))

    data3 = df['score'].max()  # 求当前列的最大值
    # data3 = df['score'].min() #最小值
    # print(data3)

    data4 = df['score'].median()  # 求当前列的中位数
    # print(data4)

    data5 = df['score'].diff()  # 求当前列前一位和后一位的差值(后-前)
    # print(data5)

    data6 = df['score'].prod()  # 当前列数据乘积
    # print(data6)

    data7 = df['score'].cumprod()  # 当前列数据累乘
    # print(data7)

    data8 = df['score'].cumsum()  # 当前列数据累加
    # print(data8)


if __name__ == '__main__':
    # one()
    # two()
    three()
