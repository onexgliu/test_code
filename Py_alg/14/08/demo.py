"""
功能：自定义挖矿函数，实现动态规划算法
参数说明：count：表示矿的数量
          TotalWorkers:表示一共工人数
          workers：表示每个矿需要的工人数
          gold：表示每个金矿黄金储量
"""
def mine(count, TotalWorkers, workers, gold):
    reserves = [[0 for j in range(TotalWorkers + 1)] for i in range(count +1)] # 置零，表示初始状态
    for i in range(1, count+1):             #遍历物每个矿，从第1个矿计算
        for j in range(1, TotalWorkers + 1): #遍历工人数
            reserves[i][j] = reserves[i - 1][j]   #定义reserves数组存储黄金的最大储存量
            # 有足够工人挖矿，遍历前一个状态考虑是否置换
            if j >= workers[i - 1] and reserves[i][j] < reserves[i - 1][j - workers[i - 1]] + gold[i - 1]:
              reserves[i][j] = reserves[i - 1][j - workers[i - 1]] +gold[i - 1]#最大存储量就是 当前存储量+剩余工人可挖存储量
    for x in reserves:                       #遍历输出挖矿网格
        print(x)
    return reserves                          #返回最大黄金的储存量
"""
功能：自定义显示输出结果函数
参数说明：count：表示矿的数量
          TotalWorkers:表示一共工人数
          workers：表示每个矿需要的工人数
          reserves：表示最大价值，即所求的结果
"""
def show(count, TotalWorkers, workers, reserves):
    x = [False for i in range(count)]                   #初始化x，使得x为假
    j = TotalWorkers                                     #工人总人数赋给变量j
    for i in range(count, 0, -1):                       #遍历每个矿
        if reserves[i][j] > reserves[i - 1][j]:                #如果reserves[i][j]单元格大于上一行同列的单元格的值，进行更新
            x[i - 1] = True
            j -= workers[i - 1]                           #工人数减去上一行同列的单元格的使用的工人数
    print('可挖最大存储量为:', reserves[count][TotalWorkers])      # 输出最大存储量的值
    print('要挖的金矿为:')
    for i in range(count):  # 遍历物品数
      if x[i]:  # 判断最大价值的物品数
        print('第', i + 1, '个矿 ', end='')  # 输出是第几个物品


count = 5                                               #一共有5个矿
TotalWorkers = 10                                       #一共有10个工人
workers = [5,5,3,4,3]                                    #每个矿需要的工人数
gold = [400,500,200,300,350]                            #每个矿的存储黄金量
reserves = mine(count, TotalWorkers, workers, gold)      #调用mine()函数动态规划算法函数
show(count, TotalWorkers, workers, reserves)             #调用show()函数输出结果
