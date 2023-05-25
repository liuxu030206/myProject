def num_to():
    # 循环打印1-10
    for i in range(10):
        print(i, end=' ')
    print()

    # 循环打印2-10
    for i in range(2, 10):
        print(i, end=' ')
    print()

    # 循环打印1-20的奇数
    for i in range(1, 20, 2):
        print(i, end=' ')
    print()

    # defined a name list
    name_list = ['刘旭', '张三', '李素']
    # 遍历列表
    for name in name_list:
        print(name, end=' ')
    print()

    # 依据索引遍历列表
    for i in range(len(name_list)):
        print(name_list[i], end=' ')
    print()


if __name__ == '__main__':
    num_to()
