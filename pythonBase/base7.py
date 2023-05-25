def tuple_():
    tu = (4, 5, 6, 9, 2, 3, 72, 38, 33)
    for t in tu:
        print(t, end=' ')
    print()

    # 存储身份信息
    tt = []
    for i in range(3):
        print(f"第{i + 1}个信息:")
        name = input("Name:")
        age = input("Age:")
        t = (name, age)
        tt.append(t)
    print(tt)

    # 字典
    dic = {}
    dic['name'] = tt[0][0]
    dic['age'] = tt[0][1]
    print(dic)


if __name__ == '__main__':
    tuple_()
