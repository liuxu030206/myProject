def str_():
    info = "weryuiwo;febuwjkgnfpowel\t\n\t\n\bf"
    print(info)
    print('计算字符串长度:', len(info))

    # 字符串替换
    print(info.replace('\n', '').replace('\t', ''))

    # 数字转化为字符串
    num = 1
    print(str(num), type(str(num)))


if __name__ == '__main__':
    str_()
