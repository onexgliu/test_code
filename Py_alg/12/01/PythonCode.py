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
def dfs(graph, start):
    stack = []                              #定义堆栈
    stack.append(start)                     #将起始顶点压入堆栈
    visited = set()                         #定义集合
    while stack:
        vertex = stack.pop()                #弹出栈顶元素
        if vertex not in visited:           #如果该顶点未被访问过
            visited.add(vertex)             #将该顶点放入已访问集合
            print(vertex,end = ' ')         #打印深度优先遍历的顶点
        for w in graph[vertex]:             #遍历相邻的顶点
            if w not in visited:            #如果该顶点未被访问过
                stack.append(w)             #把顶点压入堆栈
print("图中各顶点的邻接点：")
for key,value in graph.items():             #遍历图的字典
    print("顶点",key,"=>",end=" ")          #打印顶点
    for v in value:                         #遍历顶点的邻接点
        print(v,end=" ")                    #打印顶点的邻接点
    print()
print("深度优先遍历的顶点：")
dfs(graph,"A")                              #调用函数并设置起点为A