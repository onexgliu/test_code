graph = {                                   #定义图的字典
    "A": ["B","C"],
    "B": ["A","D","E"],
    "C": ["A","D","G"],
    "D": ["B","C","F","H"],
    "E": ["B","F"],
    "F": ["D","E","G","H"],
    "G": ["C","F","H"],
    "H": ["D","F","G"],
}
def bfs(graph, start):
    queue = []                              #定义队列
    queue.append(start)                     #将起始顶点放入队列
    visited = set()                         #定义集合
    visited.add(start)                      #将起始顶点放入已访问集合
    while queue:
        vertex = queue.pop(0)               #取出队列第一个元素
        print(vertex,end = ' ')             #打印广度优先遍历的顶点
        for w in graph[vertex]:             #遍历相邻的顶点
            if w not in visited:            #如果该顶点未被访问过
                visited.add(w)              #将该顶点放入已访问集合
                queue.append(w)             #把顶点放入队列
print("图中各顶点的邻接点：")
for key,value in graph.items():             #遍历图的字典
    print("顶点",key,"=>",end=" ")          #打印顶点
    for v in value:                         #遍历顶点的邻接点
        print(v,end=" ")                    #打印顶点的邻接点
    print()
print("广度优先遍历的顶点：")
bfs(graph,"A")                              #调用函数并设置起点为A