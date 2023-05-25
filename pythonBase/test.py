import random


def str_():
    """
    请将这个列表的空格和非汉字字符去除掉，程序效果如图
    :return:
    """
    newList = ['/n 李四', '和 ', '王五  /n', '是', ' 好朋友 ']
    new = []
    for i in range(len(newList)):
        new.append(newList[i].replace('/n', '').replace(' ', ''))
        print(new[i])
    print(new)


def shake():
    """
    请编写一个摇骰子的游戏
    :return:
    """
    num = random.randint(1, 6)
    if num == 4 or num == 5 or num == 6:
        result = '大'
    else:
        result = '小'
    print("""
    庄家开始摇色子，请稍等。。。。
    庄家摇色子完毕
    请猜大小：1：大 2：小
    """)
    user_num = int(input())
    if user_num == 1:
        user_choice = '大'
    else:
        user_choice = '小'

    print("庄家投掷的是：", num)
    if user_choice == result:
        print("猜对了")
    else:
        print("猜错了")


def sort_():
    """
    让用户任意输入5个数字，把用户输入的值存入列表，
    当用户输入完5个值后，需要把用户输入的5个值遍历出来，
    并且计算出用户输入的最大值是什么和最小值什么，在进行降序显示出来
    :return:
    """
    num_list = []
    for i in range(5):
        num = int(input(f"请输入第{i + 1}个数:"))
        num_list.append(num)
    max_num = max(num_list)
    min_num = min(num_list)
    num_list.sort(reverse=True)
    print("最大值:", max_num)
    print("最小值:", min_num)
    print("降序排列:", num_list)


if __name__ == '__main__':
    str_()
    shake()
    sort_()
