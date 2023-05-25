def lst():
    # 创建一个列表
    new_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    # 循环打印列表
    for i in range(len(new_list)):
        print(new_list[i], end=' ')
    print()

    # 打印列表
    print("列表:", new_list)

    # 访问列表第五个为元素
    print("列表第五个为元素:", new_list[4])

    # 截取列表第三个到第七个之间
    print("列表第三个到第七个之间:", new_list[2:7])

    # 更新列表第十个元素
    print("更新前第十个元素为:", new_list[9])
    new_list[9] = 100
    print("更新后第十个元素为:", new_list[9])

    # 更新列表所有值，在原有基础上+2
    print("更新前的列表:", new_list)
    for i in range(len(new_list)):
        new_list[i] = new_list[i] + 2
    print("更新后的列表:", new_list)

    # 删除列表
    del new_list[2]
    print("删除后的列表:", new_list)

    # 列表转元组
    new_tuple = tuple(new_list)
    print("转换后的元组:", new_tuple)

    # 降序排序
    new_list_2 = [4, 5, 6, 1, 2, 3, 7, 8, 9]
    new_list_2.sort(reverse=True)
    print("降序排序:", new_list_2)

    # 清空列表
    new_list_2.clear()
    print("清空后的长度:", len(new_list_2))

    # 字符串分割反转
    s = "hello world"
    s_list = s.split(" ")
    temp = ''
    temp = s_list[0]
    s_list[0] = s_list[1]
    s_list[1] = temp
    print(" ".join(s_list))


if __name__ == '__main__':
    lst()
