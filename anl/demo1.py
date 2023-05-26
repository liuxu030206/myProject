import pandas as pd


# 系列数据格式
def test1():
    name = ("张三", "李四", "王五")
    # 把列表/元组转化为序列
    data = pd.Series(name, index=[0, 1, 2])
    """
    data = pd.Series(name, index=[0,1,2])
        .Series(name, index=[]) 表示序列化， 
        name为元组/列表， 
        index为序列的下标域
        index的维度必须和name的维度相同
    """
    print(data)


# 数据帧数据格式
def test2():
    data = [("张三", 18), ("李四", 19), ("王五", 20)]
    # 把元组转化为数据帧格式
    data = pd.DataFrame(data, columns=['name', 'age'])
    """
    data = pd.DataFrame(data, columns=['name', 'age'])
        data为多维度列表/元组
        columns = ['name', 'age']为数据帧设置列名
        columns维度必须和data列维度相同
    """
    print(data)
    name = ["张三", "李四", "王五"]
    name = pd.DataFrame(name, columns=['name'])
    print(name)


# 设置数据帧的行标签
def test3():
    data = [("张三", 18), ("李四", 19), ("王五", 20)]
    # 把元组转化为数据帧格式
    data = pd.DataFrame(data, columns=['name', 'age'], index=['a', 'b', 'c'])
    """
    columns和index的维度必须和data维度相匹配
    """
    # 先找到列，再找到行
    print("访问name列的第二行的第一个值", data['name']['b'])


# 数据帧的添加和删除
def test4():
    data = [("张三", 18), ("李四", 19), ("王五", 20)]
    data = pd.DataFrame(data, columns=['name', 'age'], index=['a', 'b', 'c'])
    # 添加一列---->新列的维度与原data维度相同
    data['address'] = ['sc', 'cq', 'yn']
    # 删除一列
    del data['address']
    print(data)


# 行选中和行删除
def test5():
    data = [("张三", 18), ("李四", 19), ("王五", 20)]
    data = pd.DataFrame(data, columns=['name', 'age'], index=['a', 'b', 'c'])
    """
    行选择
        方式一：data['name']['b']--->单独的值
        方式二：data.loc['c']--->类似键值对信息
        方式三：data.loc['c']['name']---> 等价于方式一
    """
    print(data.loc['c']['name'])

    """
    行删除
        new_data = data.drop('行索引')
    """
    data = data.drop('b')
    print(data)


def writecsv():
    # .read_csv()读取csv文件
    data = pd.read_csv('D:\\桌面\\Python\\myProject\\csv_file\\birthrate.csv')
    # print(data)


    # .to_csv()写入csv文件
    data1 = [("张三", 18), ("李四", 19), ("王五", 20)]
    # 先转化为数据帧
    data1 = pd.DataFrame(data1, columns=['name', 'age'])
    data1.to_csv('D:\\桌面\\Python\\myProject\\csv_file\\info.csv', index=False)  # index=False默认不写入索引值


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    writecsv()
