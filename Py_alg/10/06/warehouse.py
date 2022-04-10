"""
功能：定义堆栈链表结点类
"""


class Node:
    def __init__(self):
        self.data = 0  # 声明堆栈数据
        self.next = None  # 堆栈在中用来指向下一个结点


top = None  # 声明顶端并初始化

"""
功能：判断堆栈链表是否为空
"""


def is_empty():
    global top  # 将top声明为全局变量
    if (top == None):  # 顶端为None
        return 1  # 返回1
    else:  # 否则
        return 0  # 返回0


"""
功能：将数据压入堆栈中
"""


def push(data):
    global top
    new_node = Node()  # 新结点
    new_node.data = data  # 将数据指定为结点的内容
    new_node.next = top  # 将新结点指向堆栈的顶端
    top = new_node  # 新结点成为堆栈的顶端


"""
功能：将数据弹出
"""


def pop():
    global top
    if is_empty():  # 判断堆栈链表为空

        print("当前堆栈链表为空")
        return -1  # 退出程序
    else:
        p = top  # 指向堆栈的顶端
        top = top.next  # 将堆栈顶端指向下一个结点
        temp = p.data  # 弹出数据
        return temp  # 将从堆栈中弹出的数据返回给主程序


# 主程序
while True:
    i = int(input("1:向堆栈中压入数据,2;堆栈中弹出,3:退出对堆栈操作：请输入您的选择: "))
    if i == 1:
        data = int(input("请输入要压入的数据:"))
        push(data)  # 调用堆栈压入数据函数

    elif i == 2:
        print("弹出的数据为", pop())  # 调用堆栈弹出数据函数
    elif i == 3:
        break  # 退出堆栈操作，即退出循环

print("---------------------------------------")
while (not is_empty()):  # 将数据陆续从顶端弹出
    print('堆栈弹出的顺序为:%d' % pop())

print("---------------------------------------")
print("可以看出：先压入的数据后弹出，后压入的数据先弹出")
