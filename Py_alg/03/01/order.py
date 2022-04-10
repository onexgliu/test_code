import random  # 导入随机数模块

num = 0  # 定义变量num
data = [0] * 50  # 定义数组
for i in range(50):  # 遍历随机生成50个数
    data[i] = random.randint(1, 100)  # 1~100之间随机生成
print("随机产生的数据内容是：")
for i in range(10):  # 遍历行
    for j in range(5):  # 遍历列
        print('%2d[%3d] ' % (i * 5 + j + 1, data[i * 5 + j]), end='')  # 按格式输出随机生成内容
    print('')

while num != -1:  # 循环输入
    find = 0  # 比较次数
    num = int(input("请输入想要查找的数据，输入-1退出程序:"))  # 数据输入
    for i in range(50):  # 循环遍历50个随机数
        if data[i] == num:  # 判断如果输入数据和data数据相等
            print("在", i + 1, "个位置找到数据", data[i])  # 输出找到的位置和数据内容
            find += 1  # 比较次数加1
    if find == 0 and num != -1:  # 判断比较次数是0且输入数据不是-1
        print("没有找到", num, "此数据")  # 提示没有找到数据
