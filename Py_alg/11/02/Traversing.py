class tree(object):  # 创建树结点
    def __init__(self, data=None, left=None, right=None):  # 结点位置
        self.data = data  # 数据域
        self.left = left  # 左子树
        self.right = right  # 右子树


class BinaryTree(object):  # 创建二叉树
    def __init__(self, root=None):  # 初始化
        self.root = root

    def is_empty(self):  # 判断是否为空
        return self.root == None

    def preorder(self, tree):  # 前序遍历
        if tree == None:  # 判断是空子树
            return
        # 不为空子树，先打印根结点，再打印左结点，后打印右结点
        print(tree.data)
        self.preorder(tree.left)
        self.preorder(tree.right)

    def inorder(self, tree):  # 中序遍历
        if tree == None:  # 判断是空子树
            return
        # 不为空子树，先打印左结点，再打印根结点，后打印右结点
        self.inorder(tree.left)
        print(tree.data)
        self.inorder(tree.right)

    def postorder(self, tree):  # 后序遍历
        if tree == None:  # 判断是空子树
            return
        # 不为空子树，先打印左结点，再打印右结点，后打印根结点
        self.postorder(tree.left)
        self.postorder(tree.right)
        print(tree.data)


n1 = tree(data="z")  # 二叉树结点z
n2 = tree(data="y")  # 二叉树结点y
n3 = tree(data="f")  # 二叉树结点f
n4 = tree(data="b", left=n1, right=None)  # 二叉树结点b,左子树是z,无右子树
n5 = tree(data="t", left=None, right=n4)  # 二叉树结点t,无左子树是,右子树为b
n6 = tree(data="c", left=None, right=n2)  # 二叉树结点c,无左子树是,右子树为y
n7 = tree(data="x", left=n6, right=n3)  # 二叉树结点x,左子树是c,右子树为f
root = tree(data="a", left=n5, right=n7)  # 根结点a,左子树是t,右子树为x

ct = BinaryTree(root)  # 创建二叉树
print('先序遍历')
ct.preorder(ct.root)  # 输出前序遍历二叉树结果
print('中序遍历')
ct.inorder(ct.root)  # 输出中序遍历二叉树结果
print('后序遍历')
ct.postorder(ct.root)  # 输出后序遍历二叉树结果
