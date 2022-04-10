# 二分查找
def search(data, key):  # 用二分查找 想要查找的数据在哪块内
    length = len(data)  # 数据列表长度
    first = 0  # 第一位数位置
    last = length - 1  # 最后一个数据位置

    print("长度:%s 分块的数据是:%s" % (length, data))  # 输出分块情况
    while first <= last:
        mid = (last + first) // 2  # 取中间位置
        if data[mid] > key:  # 中间数据大于想要查的数据
            last = mid - 1  # 将last的位置移到中间位置的前一位
        elif data[mid] < key:  # 中间数据小于想要查的数据
            first = mid + 1  # 将first的位置移到中间位置的后一位
        else:
            return mid  # 返回中间位置
    return False


# 分块查找
def block(data, count, key):  # 分块查找数据，data是列表，count是每块的长度，key是想要查找的数据
    length = len(data)  # 表示数据列表的长度
    blockLength = length // count  # 一共分的几块
    if count * blockLength != length:  # 每块长度乘以分块总数不等于数据总长度
        blockLength += 1  # 块数加1
    print("一共分", blockLength, "块")  # 块的多少
    print("分块情况如下：")
    for block_i in range(blockLength):  # 遍历每块数据
        blockData = []  # 每块数据初始化
        for i in range(count):  # 遍历每块数据的位置
            if block_i * count + i >= length:  # 每块长度要与数据长度比较，一旦大于数据长度
                break  # 就退出循环
            blockData.append(data[block_i * count + i])  # 每块长度要累加上一块的长度
        result = search(blockData, key)  # 调用二分查找的值
        if result != False:  # 查找的结果不为False
            return block_i * count + result  # 就返回块中的索引位置
    return False


data = [23, 43, 56, 78, 97, 100, 120, 135, 147, 150, 155]  # 数据列表
result = block(data, 4, 150)  # 第二个参数是块的长度，最后一个参数是要查找的元素
print("查找的值得索引位置是:", result)  # 输出结果
