"""
功能：用数组创建二叉树
参数：tree_array：存放二叉树数组
      data：数据
      length：长度
"""


def Binary_tree_create(tree_array, data, length):
    for i in range(1, length):
        index = 1  # 索引值初始化
        while tree_array[index] != 0:
            if data[i] > tree_array[index]:  # 如果数组内的值大于树根，则往右子树比较
                index = index * 2 + 1
            else:  # 如果数组内的值小于或等于树根，则往左子树比较
                index = index * 2
        tree_array[index] = data[i]  # 把数组值放入二叉树


length = 9  # 长度为9
data = [0, 3, 2, 6, 7, 4, 5, 1, 9]  # 原始数组
tree_array = [0] * 16  # 存放二叉树数组
print('原始数组内容：')
for i in range(length):
    print('%2d ' % data[i], end='')
print('')
Binary_tree_create(tree_array, data, 9)
print('二叉树内容：')
for i in range(1, 16):
    print('%2d ' % tree_array[i], end='')
print()
