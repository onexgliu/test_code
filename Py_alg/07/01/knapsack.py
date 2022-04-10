"""
功能：自定义背包函数，实现动态规划算法
参数说明：count：表示物品件数
          TotalWeight:表示背包的总容量
          weight：表示每件物品的重量
          cost：表示每件物品的价值
"""
def bag(count, TotalWeight, weight, cost):
    value = [[0 for j in range(TotalWeight + 1)] for i in range(count +1)] # 置零，表示初始状态
    for i in range(1, count+1):#遍历物品件数，从第1件物品计算
        for j in range(1, TotalWeight + 1):#遍历背包容纳量，从重量为1开始计算
            value[i][j] = value[i - 1][j]#定义value数组存储最大价值
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= weight[i - 1] and value[i][j] < value[i - 1][j - weight[i - 1]] + cost[i - 1]:
                value[i][j] = value[i - 1][j - weight[i - 1]] +cost[i - 1]#最大价值就是 当前物品的价值+剩余空间的价值
    for x in value:#遍历输出背包网格
        print(x)
    return value#返回最大价值
"""
功能：自定义显示输出结果函数
参数说明：count：表示物品件数
          TotalWeight:表示背包的总容量
          weight：表示每件物品的重量
          value：表示最大价值，即所求的结果
"""
def show(count, TotalWeight, weight, value):
    x = [False for i in range(count)]#初始化x，使得x为假
    j = TotalWeight#背包的容量赋给变量j
    for i in range(count, 0, -1):#遍历每个物品
        if value[i][j] > value[i - 1][j]:#如果value[i][j]单元格大于上一行同列的单元格的价值，进行更新
            x[i - 1] = True
            j -= weight[i - 1]#总容量减去上一行同列的单元格的重量
    print('最大价值为:', value[count][TotalWeight])  # 输出最大价值的值
    print('背包中所装物品为:')
    for i in range(count):#遍历物品数
        if x[i]:#判断最大价值的物品数
            print('第', i + 1, '个 ', end='')#输出是第几个物品


count = 3#一共有3件物品
TotalWeight = 4#背包的总容量是4
weight = [1, 4, 3]#每个物品的重量
cost = [4900, 7800, 5600]#每个物品的价值
value = bag(count, TotalWeight, weight, cost)#调用bag()函数动态规划算法函数
show(count, TotalWeight, weight, value)#调用show()函数输出结果
