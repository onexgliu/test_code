def Kruskal(vertex_list, edges):
    all_vertex_list = vertex_list  # 获取所有顶点列表
    tree_name_list = []  # 树名称列表
    for n in all_vertex_list:
        tree_name_list.append(n)  # 初始化树名称列表
    MST = []  # 最小生成树列表
    edges = sorted(edges, key=lambda element: element[2])  # 对所有边按权重升序排列
    while len(MST) != len(vertex_list) - 1:  # 最小生成树中的边为n-1时退出循环
        element = edges.pop(0)  # 获取权重最小的边
        vertex_start = element[0]  # 边的起始顶点
        vertex_end = element[1]  # 边的终止顶点
        name1 = tree_name_list[all_vertex_list.index(vertex_start)]  # 起始顶点所在树的名称
        name2 = tree_name_list[all_vertex_list.index(vertex_end)]  # 终止顶点所在树的名称
        # 如果两个顶点不在同一树中，即加入边后不会形成回路
        if name1 != name2:
            MST.append(element)  # 把边加入最小生成树列表
            # 将所有树名称name2改为name1
            for n in range(0, len(tree_name_list)):
                if tree_name_list[n] == name2:
                    tree_name_list[n] = name1
    return MST  # 返回最小生成树列表


def main():
    vertex_list = ["A", "B", "C", "D", "E", "F", "G"]  # 图的所有顶点列表
    # 图的所有边组成的列表
    edges = [("A", "B", 10), ("A", "F", 3),
             ("A", "G", 6), ("B", "C", 7),
             ("B", "G", 8), ("C", "D", 9),
             ("C", "G", 5), ("D", "E", 15),
             ("D", "G", 10), ("E", "F", 12),
             ("E", "G", 13), ("F", "G", 9)]
    tree_list = Kruskal(vertex_list, edges)  # 调用函数
    print("实现各城镇公路互通的方案如下：")
    for n in tree_list:
        print("({:s}—{:s})".format(n[0], n[1]))
    total_price = 0  # 最低成本初始化
    for n in tree_list:
        total_price += n[2]  # 计算最低成本
    print("\n各城镇公路互通的最低成本：" + str(total_price))


if __name__ == '__main__':
    main()  # 调用函数
