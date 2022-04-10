import random
def get_times(low,high):
    times = 0       # 可猜数字的次数
    # 获取可猜数字的次数
    while True:
        mid = (low + high) // 2
        high = mid
        times += 1
        if mid == low:
            break
    return times
def guess(random_number,times):
    print("您有{}次猜数字的机会！".format(times))
    count = 1       # 猜数字的次数
    while times != 0:
        guess_number = int(input("第{}次机会，请输入整数（0~100）：".format(count)))
        times -= 1  # 每猜一次，可猜数字的次数就减1
        if guess_number < random_number:    # 如果输入的数字小于随机整数
            print("数字太小了！")
        elif guess_number > random_number:  # 如果输入的数字大于随机整数
            print("数字太大了！")
        else:
            print("您猜对了！一共猜了{}次！".format(count))
            break
        count += 1  # 猜数字的次数加1
    else:
        print("机会用完了，游戏结束！正确答案为{}".format(random_number))
if __name__ == "__main__":
    low = 0         # 数字范围的最小值
    high = 100      # 数字范围的最大值
    times = get_times(low,high) # 调用函数获取可猜数字的次数
    random_number = random.randint(low, high)   # 生成一个随机整数
    guess(random_number,times)
