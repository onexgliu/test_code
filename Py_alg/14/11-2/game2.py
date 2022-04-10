import random


def take_match(match):
    count = 0
    take_num = 0  # 保存抽取火柴的数量
    while match > 1:  # 火柴剩一根时结束循环
        count += 1
        print("第{}轮抽取火柴：".format(count))
        # 计算机抽取火柴
        if match > 5:  # 如果剩余火柴数多于5个
            take_num = random.randint(1, 4)  # 随机抽取火柴数量
        else:
            take_num = match - 1  # 抽取后剩最后一根火柴
        match -= take_num  # 还剩多少根火柴
        print("计算机抽取" + str(take_num) + "根火柴")
        if match == 1:
            print("还剩最后一根火柴，你输了！")
        # 真人抽取火柴
        while True:
            take_num = int(input("请输入抽取火柴数："))
            if take_num > 0 and take_num <= 4:  # 限制抽取火柴数
                break
        match -= take_num  # 还剩多少根火柴
        if match == 1:
            print("还剩最后一根火柴，你赢了！")
        print("-" * 23)


take_match(21)  # 调用函数
