def fibonacci_search(data, key):
    # 需要一个现成的斐波那契列表。其最大元素的值必须超过查找表中元素个数的数值。
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765]
    low = 0  # 低位
    high = len(data) - 1  # 高位

    # 为了使得查找表满足斐波那契特性，在表的最后添加几个同样的值
    # 这个值是原查找表的最后那个元素的值
    # 添加的个数由F[k]-1-high决定
    k = 0
    while high > F[k] - 1:
        k += 1
    i = high  # 将i定位到high的位置
    while F[k] - 1 > i:  # 添加数据
        data.append(data[high])  # 追加到high之后的位置上
        i += 1
    print("添加后的数据", data)  # 输出追加后的数据

    # 算法主逻辑,count用于展示循环的次数。
    while low <= high:  # 满足低位小于等于高位
        # 为了防止F列表下标溢出，设置if和else
        if k < 2:
            mid = low
        else:
            mid = low + F[k - 1] - 1

        print("低位位置：%s, 中间位置：%s,高位位置：%s" % (low, mid, high))  # 输出每次分割情况
        if key < data[mid]:  # 目标数据小于中间值数据，在左侧寻找
            high = mid - 1  # 高位位置移到mid-1的位置
            k -= 1  # 下标k此时减1
        elif key > data[mid]:  # 目标数据大于中间值数据，在右侧寻找
            low = mid + 1  # 低位位置移到mid+1的位置
            k -= 2  # 下标k此时减2
        else:  # 否则
            if mid <= high:  # 中间值小于等于mid
                return mid  # 此时的结果是mid就是目标值得位置，返回mid即可
            else:  # 如果mid大于了高位位置值
                return high  # 此时的结果直接返回high的值
    return False


# 验证数据
data = [9, 10, 13, 15, 22, 29, 37, 48, 53]  # 数据列表
key = int(input("请输入想要查找的数据："))
result = fibonacci_search(data, key)  # 调用斐波那契查找函数
print("目标数据", key, "的位置是", result)  # 输出结果
