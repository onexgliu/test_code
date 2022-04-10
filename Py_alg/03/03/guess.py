def insret_seach(data,num):#自定义插补查找函数
    low=0#定义变量表示最低位
    high=8#定义变量表示最高位
    print("正在查找......")#提示
    while low<=high and num!=-1:#循环判断低位小于等于高位且键值不等于-1
        mid=low+int((num-data[low])*(high-low)/(data[high]-data[low]))#用插补查找核心 计算出边界位置
        if num==data[mid]:#如果键值等于边界值
            return mid#返回边界位置
        elif num<data[mid]:#如果键值小于边界值
            print('%c介于位置%d[%c]和边界值%d[%c]之间，找左半边'%(num,low+1,data[low],mid+1,data[mid]))#输出在左半边查找
            high=mid-1#最高位等于边界位置减1
        elif num>data[mid]:#如果键值大于边界值
            print('%c介于边界值位置%d[%c]和%d[%c]之间，找右半边'%(num,mid+1,data[mid],high+1,data[high]))#输出在右半边查找
            low=mid+1#最低位等于边界位置加1
    return -1# 自定义函数到此结束


num = 0  # 定义变量，用来输入键值
data = ['a','b','c','d','e','f','g','h','m']  # 定义数列

print("数据内容是：")
for i in range(1):  # 遍历行
    for j in range(9):  # 遍历列
        print(' %d[%c]' % (i * 9 + j + 1, data[i * 9 + j]), end='')  # 输出数列
    print('')

while True:  # 循环查找
    number = 0  # 定义变量用来存储查找结果
    num = int(input("请输入查找键值，输入-1退出程序："))  # 输入查找键值
    if num == -1:  # 判断键值是否是-1
        break  # 若为-1，跳出循环
    number = insret_seach(data, num)  # 调用自定义的查找函数——search()函数
    if number == -1:  # 判断查找结果是否是-1
        print('没有找到[%c]' % num)  # 若为-1，提示没有找到值
    else:
        print('在%d个位置找到[%c]' % (number + 1, data[number]))  # 若不为-1，提示查找位置

