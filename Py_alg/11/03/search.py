class tree:
    def __init__(self):
        self.data = 0  # 数据域
        self.left = None  # 左子结点指针
        self.right = None  # 右子结点指针


"""
功能：创建二叉树
参数：root：表示根结点
      value：保存的值
"""


def creat_tree(root, value):
    new_node = tree()  # 创建树结点
    new_node.data = value  # 数据域
    new_node.left = None  # 左子树
    new_node.right = None  # 右子树
    if root == None:  # 如果根结点是空，这种情况就是空二叉树
        root = new_node  # 直接将根结点给新树
        return root  # 返回根结点
    else:
        current = root  # 当前结点
        while current != None:
            backup = current
            if current.data > value:  # 大于保存数值
                current = current.left  # 放在左子树
            else:  # 否则
                current = current.right  # 放在右子树
        if backup.data > value:
            backup.left = new_node  # 将数据左子树放在新树中
        else:
            backup.right = new_node  # 将数据右子树放在新树中
    return root


def search(p, val):  # 查找二叉树中某个值
    i = 1
    while True:  # 循环查找
        if p == None:  # 没找到就返回None
            return None
        if p.data == val:  # 查找值等于结点值
            print("共计查找", i, "次")
            return p
        elif val < p.data:  # 查找值小于结点值
            p = p.left  # 向左子树查找
        else:  # 否则
            p = p.right  # 向右子树查找
        i += 1  # 查找次数加1


# 主程序
arr = [6, 3, 8, 2, 5, 1, 7]
p = None
print('数据内容是')
for i in range(7):
    p = creat_tree(p, arr[i])  # 建立二叉树
    print('%2d ' % arr[i], end='')
print()
data = int(input('请输入查找值：'))
if search(p, data) != None:  # 在二叉树中查找
    print("您要找的值", data, "找到了^_^")
else:
    print("您要找的值没找到^ ^")
