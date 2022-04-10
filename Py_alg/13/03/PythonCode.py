def maxSubList(theList):  # 定义函数并传入参数theList
    if theList == []:  # 如果列表为空则终止程序
        return
    if len(theList) == 1:  # 如果列表只有一个元素则获取该元素
        return theList[0]
    sep = len(theList) // 2  # 将列表一分为二
    leftMaxSum = maxSubList(theList[:sep])  # 获取左子列表的最大和
    rightMaxSum = maxSubList(theList[sep:])  # 获取右子列表的最大和
    leftSum = 0  # 记录中点左边已遍历过的数值的和
    maxLeft = 0  # 记录中点左边的和的最大值
    rightSum = 0  # 记录中点右边已遍历过的数值的和
    maxRight = 0  # 记录中点右边的和的最大值
    for i in range(sep - 1, -1, -1):  # 遍历中点左边的值
        leftSum += theList[i]  # 对数值按从右到左的顺序累加，记录每一次的和
        maxLeft = max(leftSum, maxLeft)  # 取这些累加和的最大值
    for i in range(sep, len(theList)):  # 遍历中点右边的值
        rightSum += theList[i]  # 对数值按从左到右的顺序累加，记录每一次的和
        maxRight = max(rightSum, maxRight)  # 取这些累加和的最大值
    return max(leftMaxSum, maxLeft + maxRight, rightMaxSum)  # 获取三个可能值中的最大值


sList = [3, -7, 6, -2, 5, 1, -3, 2]  # 定义数值列表
print("数值列表：", sList)  # 输出数值列表
maxSum = maxSubList(sList)  # 调用函数
print("连续子列表最大和：", maxSum)  # 打印连续子列表最大和
