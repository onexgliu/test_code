def insert(data):  # 自定义一个插入排序法函数
    for i in range(5):  # 遍历新数据
        temp = data[i]  # temp用来暂存数据
        j = i - 1
        while j >= 0 and temp < data[j]:  # 循环排序，判断条件是数据的下标值要大于等于0且暂存数据小于原数据
            data[j + 1] = data[j]  # 把所有元素往后移一位
            j -= 1  # 下标减1
        data[j + 1] = temp  # 最小的数据插入最前一个位置
        print('第 %d 次排序之后的结果是' % (i + 1), end='')  # 提示
        for j in range(5):  # 遍历每次排序的结果
            print('%3d' % data[j], end='')  # 输出结果
        print()  # 输出空行


data = [58, 29, 86, 69, 10]  # 创建数列并初始化
print("原始数据为：")  # 提示
for i in range(5):  # 遍历原有数据
    print('%3d' % data[i], end='')  # 输出结果
print('\n---------------------------')  # 输出分界符
insert(data)  # 调用选择排序法函数
print('\n---------------------------')  # 输出分界符
print("排序之后的数据为：")  # 提示
for i in range(5):  # 遍历排序好的新数列的数据
    print('%3d' % data[i], end='')  # 输出结果
print('')  # 输出空行
