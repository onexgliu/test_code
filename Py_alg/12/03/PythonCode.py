# 存储BFS结果
class BFSResult:
    def __init__(self):
        self.visited = []  # 已访问顶点
        self.parent = {}  # 上一级顶点


# 广度优先搜索
def bfs(graph, start):
    r = BFSResult()
    r.parent = {start: None}  # 起始顶点的上一级顶点为None
    r.visited.append(start)  # 起始顶点加入已访问顶点列表
    fronter = [start]
    while fronter:
        next = []
        for u in fronter:  # 遍历上一级顶点
            for v in graph[u]:  # 遍历当前顶点的相邻顶点
                if v not in r.visited:  # 如果该顶点未被访问
                    r.visited.append(v)  # 将顶点加入已访问顶点列表
                    r.parent[v] = u  # 定义当前顶点的上一级顶点
                    next.append(v)
        fronter = next
    return r


# 返回最短路径
def find_shortest_path(bfs_result, end):
    start_vertex = bfs_result.visited[0]  # 起始顶点
    vertex_list = [end]  # 最短路径顶点列表
    if end != start_vertex:  # 如果设置的终点不是起始顶点
        parent_vertex = bfs_result.parent[end]  # 获取终点的上一级顶点
        vertex_list.insert(0, parent_vertex)  # 将上一级顶点加入最短路径顶点列表
        while parent_vertex != start_vertex and parent_vertex != None:
            parent_vertex = bfs_result.parent[parent_vertex]
            vertex_list.insert(0, parent_vertex)
    return vertex_list  # 返回最短路径顶点列表


if __name__ == '__main__':
    graph = {  # 定义图的字典
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['A', 'G'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'I'],
        'G': ['C', 'D', 'H'],
        'H': ['G', 'I'],
        'I': ['F', 'H', 'J'],
        'J': ['I']
    }
    bfs_result = bfs(graph, 'A')
    print('A城市到J城市的最短路径：')
    result = find_shortest_path(bfs_result, 'J')
    print(' -> '.join(result))
