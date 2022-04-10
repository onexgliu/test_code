def radix_sort(data):  # 基数排序,参数data是待排序数列
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(data)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list = [[] for x in range(10)]  # 初始化桶数组,因为每一位数字都是0~9，故建立10个桶,列表中包含十个列表元素
        for x in data:  # 找数据
            bucket_list[int(x / (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
        print(bucket_list)  # 打印每次的桶情况
        data.clear()  # 将原data置空
        for x in bucket_list:  # 放回原data序列
            for y in x:  # 遍历排序后的结果
                data.append(y)  # 放数据
        i += 1  # 执行一次，向后继续拿数据执行循环


data = [410, 265, 52, 530, 116, 789, 110]  # 待排序列表
radix_sort(data)  # 调用基数排序函数
print(data)  # 输出排序结果
