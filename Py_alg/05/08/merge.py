def merge_sort(data):  # 自定义的合并排序法函数
    if len(data) <= 1:  # 判断列表元素是否小于等于1
        return data  # 当列表元素只有一个的时候，直接返回
    mid = len(data) // 2  # 分隔长度计算，整个数据的长度除以2取整
    left = data[:mid]  # 左半边数据
    right = data[mid:]  # 右半边数据

    left = merge_sort(left)  # 调用merge_sort函数继续对左半边分隔并排序
    right = merge_sort(right)  # 调用merge_sort函数继续对右半边分隔并排序
    # 递归的进行排序
    result = []  # 用来存储结果值
    while left and right:  # 循环合并，判断条件是：左下标和右下标是否为真
        if left[0] >= right[0]:  # 判断左边数大于右边数
            result.append(left.pop(0))  # 结果增加left[0]的值
        else:
            result.append(right.pop(0))  # 结果增加right[0]的值
    if left:  # 如果left的值为真
        result += left  # 结果显示左侧数据
    if right:  # 如果right的值为真
        result += right  # 结果显示右侧数据
    return result  # 返回排序后的结果


data = [2750, 3429, 1632, 4019, 3698]  # 创建数列并初始化
print("五大品牌手机销售量如下：", data)  # 输出原始数据
print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')  # 输出分界符
print("从高到低排序之后的销售量如下：", merge_sort(data))  # 调用函数，输出排序好的数据
print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')  # 输出分界符
