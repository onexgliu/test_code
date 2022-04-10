import random  #导入随机模块
import math    #导入数学模块
"""
功能：网格初始化
参数：d表示矩阵的大小
"""
def InitGrid(d):
    grid = [[(x + 1, y + 1) for y in range(d)] for x in range(d)]#利用列表推导式初始化网格
    return grid                         #返回初始化的网格

"""
功能：指定行过滤出可选位置并随机选取一个，作为本行“皇后”的填入位置
参数：grid：网格矩阵
      rowIndex: 指定矩阵的某一行的序号
      position：已被选的位置
      backtracking: 回溯时的排除项列表
"""
def fill(grid, rowIndex, position, backtracking):
  row = grid[rowIndex] #取到某行
  optional = []   #在后续过程中保存本行过滤完的可选位置
  if len(position) != 0:#判断已被选择的位置不为0,进行回溯
    for column in row:   #遍历本行的每一项
      available = True  #这个变量标志了该位置是否可用，初始化的时候是True，可用
      for item in position: #遍历已被选的位置
        #只要有一个出现同行、同列、同对角线，或位于排除项列表中时，将available标记为不可用
        if column[1] == item[1] or column[0]+column[1] == item[0]+item[1] or \
          column[0]-column[1] == item[0]-item[1] or column in backtracking:
          available = False
      if available:  #该位置可用，添加进可用项列表里
          optional.append(column)
  else:
      optional = row #行保存到可选位置的列表中
  if len(optional) == 0:  #死解，返回0，指示不成功
    return 0
  else: # 活解，随机挑选位置点，返回1，指示成功
    randomIndex = math.floor(len(optional) * random.random())#随机位置点
    pick = optional[randomIndex]#挑选位置
    position.append(pick)#把这个位置点添加到可选位置的列表中
    return 1

"""
功能：根据最终结果用网格展示出来
参数：positions: 最终挑选的位置列表
"""
def show(positions):
    figure = ''#初始化
    for row in range(8):#遍历行
        for line in range(8):#遍历列
            if (row + 1, line + 1) in positions:#判断行列在可选位置上
                figure += 'Q  '#就在网格中添加Q(表示皇后)
            else:#否则
                figure += '■ '#就在网格中添加方块■
        figure += '\n'#遍历4列之后再换行遍历
    return figure#返回网格


gird = InitGrid(8)#初始化4X4网格
position = []#保存本行过滤完的可选位置的列表
backtracking = [[] for i in range(8)]#回溯4X4网格的列表
row = 0#行
while row < 8:#循环4行
    success = fill(gird, row, position, backtracking[row])#调用fill()函数填入皇后
    if success == 1:
        row += 1  # 没有遇到死解，继续往下
    else:
        row -= 1 # 遇到了死解，回退到上一行并且将死解的点存入排除项中，重新选点
        backtracking[row].append(position.pop())
        if row < 7: # 由于是自上而下选点的方式，当上一行的点重新选取时，后一行的排除项已经没有意义了，清空
            backtracking[row + 1] = []
print(show(position))# 调用show()函数展示出网格
