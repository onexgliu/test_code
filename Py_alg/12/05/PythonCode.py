def prim(graph):
    vertex_list = ["A", "B", "C", "D"]  # 顶点列表
    cost = [6, 5, 12, 3]  # 费用列表
    visited = [0, 0, 0, 0]  # 顶点是否已访问的列表，0表示未访问
    n = len(vertex_list)  # 图的顶点个数
    for i in range(0, n):
        k = 0
        min = float("inf")  # 最小值初始化
        for j in range(0, n):
            if (not visited[j] and cost[j] < min):
                min = cost[j]  # 获取费用列表最小值
                k = j  # 获取费用列表最小值的索引
        visited[k] = 1  # 标记为已访问
        for j in range(0, n):
            if (not visited[j] and graph[k][j] < cost[j]):
                cost[j] = graph[k][j]  # 更新费用列表
    return cost


def main():
    graph = [[0, 6, 8, 5],  # 图的权重列表
             [6, 0, 9, 7],
             [8, 9, 0, 10],
             [5, 7, 10, 0]]
    lowcost = prim(graph)  # 调用函数
    total_cost = 0  # 总费用初始化
    for n in lowcost:
        total_cost += n  # 计算总费用
    print("建立引水工程最小费用列表：" + str(lowcost))
    print("四个地区建立引水工程最小费用为" + str(total_cost))


if __name__ == '__main__':
    main()  # 调用函数
