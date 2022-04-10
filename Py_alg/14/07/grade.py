def scoring(num):
    flag = True
    while flag:  # flag为False时退出循环
        try:
            score = float(input("第{}位评委打分（0~10）：".format(num)))
            # 判断输入的分数是否合法
            if score >= 0 and score <= 10 and score % 0.5 == 0:
                flag = False
            else:
                print("输入错误，请重新输入")
                flag = True
        except:
            print("输入错误，请重新输入")
            flag = True
    return score


if __name__ == "__main__":
    sum = 0  # 求和
    high = 0  # 记录最高分
    low = 10  # 记录最低分
    for i in range(7):
        score = scoring(i + 1)  # 获取评委打分
        sum += score  # 计算分数之和
        if score < low:
            low = score  # 获取最低分
        elif score > high:
            high = score  # 获取最高分
    difficulty = 3.0  # 难度系数
    final = (sum - high - low) * difficulty / 5 * 3  # 计算最后得分
    print("该选手第一跳的最后得分是{:.1f}分".format(final))
