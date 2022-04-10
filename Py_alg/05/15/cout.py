def countSort(data, maxValue):  # 定义计数排序，data是列表数据，maxValue表示最大值
    bucketLen = maxValue + 1  # 定义桶的长度是最大值加1，桶号从0开始
    bucket = [0] * bucketLen  # 初始化桶
    cout = 0  # 计数个数
    arrLen = len(data)  # 列表长度
    for i in range(arrLen):  # 遍历列表
        if not bucket[data[i]]:  # 列表数据不为桶号
            bucket[data[i]] = 0  # 这时初始化从0将列表数据做桶号
        bucket[data[i]] += 1  # 桶号依次加1
    for j in range(bucketLen):  # 遍历桶
        while bucket[j] > 0:  # 将列表数据放在对应桶号内
            data[cout] = j
            cout += 1  # 计数个数加1
            bucket[j] -= 1  # 个数减一，下一个相同的元素往前排
    return data  # 返回排序后的列表


data = [1, 2, 4, 1, 3, 5, 2, 2, 7, 3, 4]
print("排序前列表数据：")
for i in range(11):
    print("%2d" % data[i], end='')
print()
data2 = countSort(data, 7)  # 调用计数排序函数
print("排序后列表数据：")
for j in range(11):
    print("%2d" % data2[j], end='')
