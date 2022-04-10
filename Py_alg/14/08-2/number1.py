target_number = int(input("请输入要猜的整数（0~100）:"))
low = 0  # 最小值
high = 100  # 最大值
count = 0  # 猜数字的次数
guess = 0  # 每一轮猜的数字
guess_list = []  # 每一轮猜的数字组成的列表
while guess != target_number:
    guess = (low + high) // 2  # 二分法猜数字
    guess_list.append(str(guess))  # 将数字添加到列表
    if guess > target_number:
        high = guess  # 将中间值作为最大值
    else:
        low = guess  # 将中间值作为最小值
    count += 1  # 猜数字的次数加1
print("一共猜了{}次".format(count), end="，")
print("数字分别是" + "、".join(guess_list))
