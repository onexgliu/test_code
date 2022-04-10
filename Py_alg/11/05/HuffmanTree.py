class Node():  # 创建树结点
    def __init__(self, item):
        self.item = item  # 数值
        self.isin = False  # 加入数据的判断
        self.left = None  # 左子树
        self.right = None  # 右子树


class HuffmanTree():  # 创建哈夫曼树
    def __init__(self, Have):
        self.list = []  # 创建列表
        for x in range(0, len(Have)):  # 遍历哈夫曼树长度
            self.list.append(Node(Have[x]))  # 向列表中添加哈夫曼树结点
        K = Node(float('inf'))  # 在结点中取值
        while len(self.list) < 2 * len(Have) - 1:  # 在哈夫曼树取叶子结点
            h1 = h2 = K  # 取值
            for x in range(0, len(self.list)):  # 遍历
                if h1.item > self.list[x].item and (self.list[x].isin is False):  # 取的数值h1大于列表数据且不在列表中
                    h2 = h1  # 将h1给h2
                    h1 = self.list[x]  # 将列表数给h1
                elif h2.item > self.list[x].item and (self.list[x].isin is False):  # 取的数值h2大于列表数据且不在列表中
                    h2 = self.list[x]  # 将列表数给h2

            H = Node(h1.item + h2.item)  # 将h1和h2数据相加成为哈夫曼树结点
            H.right = h1  # 将h1给哈夫曼树右子树
            H.left = h2  # 将h2给哈夫曼树左子树
            self.list.append(H)  # 在列表中添加哈夫曼树
            h1.isin = h2.isin = True  # 经过以上操作 h1、h2此时在哈夫曼树中
            print(' h1=%d h2=%d h1+h2=%d' % (h1.item, h2.item, H.item))  # 输出哈夫曼树相加过程


Have = [5, 6, 8, 12, 3, 1]  # 数据
print("创建哈夫曼树每轮相加过程如下：")
h = HuffmanTree(Have)  # 将上面的数据创建为哈夫曼树
print("哈夫曼树创建完成")  # 提示
