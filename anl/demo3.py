import pandas as pd


def t1():
    data = [("张三", 18, 100), ("李四", 19, 60), ("王五", 20, 87)]
    df = pd.DataFrame(data, columns=['name', 'age', 'score'])
    print(df)
    # itertuples迭代器
    for i in df.itertuples():
        print(i.name)
        # print(i.score)
    print("------------------------------------------------------------")

    # 求出最高分学生姓名
    score_max = df['score'].max()
    for i in df.itertuples():
        if i.score == score_max:
            print("最高分的学生:", i.name)
    print("------------------------------------------------------------")

    # iterrows迭代器
    for index, row in df.iterrows():
        print("index:", index)
        print("row:\n", row)
        print("name:", row['name'])
        print("--------------")


if __name__ == '__main__':
    t1()
