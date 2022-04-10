import math
vertexes = ['A', 'B', 'C', 'D', 'E']        #顶点列表
#初始化路径矩阵
dis = [[0, 10, math.inf, 7, math.inf],
       [10, 0, 6, 19, math.inf],
       [math.inf, 6, 0, 8, 16],
       [7, 19, 8, 0, 5],
       [math.inf, math.inf, 16, 5, 0]]
vertex_num = len(vertexes)                  #顶点个数
for i in range(vertex_num):
    for j in range(vertex_num):
        for k in range(vertex_num):
            #dis[i][j]表示i到j的最短距离
            #dis[i][k]表示i到k的最短距离
            #dis[k][j]表示k到j的最短距离
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]) #找到两顶点间的最短距离并更新
print('最短路径矩阵如下：')
print('====================================')
print('      A     B     C     D     E')    #打印横向各顶点
for i in range(vertex_num):
    print(vertexes[i], end=' ')             #打印纵向各顶点
    for j in range(vertex_num):
        print('%5d ' %dis[i][j], end='')
    print()