import random
def take_match(match):
    id = 0          # 根据id切换玩家
    take_num = 0    # 保存抽取火柴的数量
    while match >= 1:       # 火柴全部取完时结束循环
        id += 1             # id值加1
        if id % 2 == 1:     # 如果id值是奇数
            gamer = "甲"     # 当前玩家为甲
            if match > 5:   # 如果火柴数多于5个
                take_num = random.randint(1,4)    # 随机抽取火柴数量
            else:
                take_num = 1        # 抽取最后一根火柴
        else:
            gamer = "乙"     # 当前玩家为乙
            take_num = 5 - take_num     # 玩家B抽取火柴数量
        match -= take_num   # 还剩多少火柴
        # 格式化输出玩家名称、抽取火柴数量和剩余火柴数量
        print("{:>2s}{:>11d}{:>15d}".format(gamer, take_num, match))
print("玩家{:3s}抽取火柴数量{:3s}剩余火柴数量".format("", ""))
print("-" * 34)
take_match(21)              # 调用函数
