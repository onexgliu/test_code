maxValue = float("inf")                         #设置最大值为无穷大
graph = [[0,9,maxValue,maxValue,maxValue,8,5],    #图的权重列表
         [9,0,6,maxValue,maxValue,maxValue,maxValue],
         [maxValue,6,0,7,maxValue,maxValue,maxValue],
         [maxValue,maxValue,7,0,13,maxValue,10],
         [maxValue,maxValue,maxValue,13,0,12,15],
         [8,maxValue,maxValue,maxValue,12,0,maxValue],
         [5,maxValue,maxValue,10,15,maxValue,0]]
def prim(graph,start):
    vertex_list = ["A","B","C","D","E","F","G"] #顶点列表
    tree_vertex_list = []                       #最小生成树顶点列表
    tree_vertex_list.append(start)              #最小生成树第一个顶点
    closest = []                                #最小生成树顶点索引列表
    lowcost = []                                #最小生成树各顶点与其他顶点的距离
    n = len(vertex_list)                        #图的顶点个数
    index = vertex_list.index(start)            #起始点的索引
    for i in range(0,n):
        lowcost.append(graph[index][i])         #初始化lowcost列表
        closest.append(index)                   #初始化closest列表
    for i in range(1,n):                        #插入n-1个顶点
        k = 0
        min = maxValue
        for j in range(0,n):
            if(lowcost[j]!=0 and lowcost[j]<min):
                min = lowcost[j]        #获取插入最小生成树的权重最小顶点的权重
                k = j                   #获取插入最小生成树的权重最小顶点的索引
        tree_vertex_list.append(vertex_list[k]) #加入最小生成树顶点列表
        print(vertex_list[closest[k]]+'—'+vertex_list[k]+'权重：'+str(lowcost[k]))#打印边的权重
        lowcost[k] = 0                          #最小生成树到该顶点距离
        for j in range(0,n):
            if(lowcost[j]!=0 and graph[k][j]<lowcost[j]):
                lowcost[j] = graph[k][j]        #更新插入顶点后的lowcost列表
                closest[j] = k                  #更新插入顶点后的closest列表
    print("最小生成树顶点："+str(tree_vertex_list)) #打印最小生成树各顶点
prim(graph,"A")                                     #调用函数并设置起始顶点为A