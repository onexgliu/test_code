def search(data, num):  # 定义查找函数，参数是原数列data和键值num
    low = 0  # 定义变量用来表示低位
    high = 8  # 定义变量用来表示高位
    print("正在查找.......")  # 提示
    while low <= high and num != -1:
        mid = int((low + high) / 2)  # 取中间位置
        if num < data[mid]:  # 判断数据小于中间值
            print(
                '%d 介于故障点位置%d[%d]和中间故障点位置%d[%d]之间，找左半边' % (num, low + 1, data[low], mid + 1, data[mid]))  # 输出位置再数列中的左半边
            high = mid - 1  # 最高位变成了中间位置减1
        elif num > data[mid]:  # 判断数据大于中间值
            print('%d 介于中间故障点位置%d[%d]和故障点位置%d[%d]之间，找右半边' % (
            num, mid + 1, data[mid], high + 1, data[high]))  # 输出位置再数列中的右半边
            low = mid + 1  # 最低位变成了中间位置加1
        else:  # 判断数据等于中间值
            return mid  # 返回中间位置
    return -1  # 自定义函数到此结束


num = 0  # 定义变量，用来输入键值
data = [12, 45, 56, 66, 77, 80, 97, 101, 120]  # 定义数列
print("疑似故障点如下：")
for i in range(1):  # 遍历行
    for j in range(9):  # 遍历列
        print(' %d[%d]' % (i * 9 + j + 1, data[i * 9 + j]), end='')  # 输出数列
    print('')

while True:  # 循环查找
    number = 0  # 定义变量用来存储查找结果
    num = int(input("请输入故障点的位置，输入-1退出程序："))  # 输入查找键值
    if num == -1:  # 判断键值是否是-1
        break  # 若为-1，跳出循环
    number = search(data, num)  # 调用自定义的查找函数——search()函数
    if number == -1:  # 判断查找结果是否是-1
        print('没有找到[%d]故障点' % num)  # 若为-1，提示没有找到值
    else:
        print('在%d个位置找到[%d]故障点' % (number + 1, data[number]))  # 若不为-1，提示查找位置
