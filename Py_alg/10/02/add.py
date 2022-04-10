"""
功能：定义结点类，作用是指向下一个结点
"""
class Node():
    def __init__(self, elem):
        self.elem = elem
        self.next = None


"""
功能：定义链表
"""
class LinkList(object):
    def __init__(self,node=None): #使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node   # __表示私有属性，不对外开放

    """
    功能：判断链表是否为空
    """
    def is_empty(self):
      return self.__head == None

    """
    功能：求链表长度
    """

    def LinkList_length(self):
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    """
    功能：遍历整个链表
    """

    def LinkList_travel(self):
        cur = self.__head  # 指向头结点

        while cur != None:
             print(cur.elem, end=' ')  # 输出链表元素
             cur = cur.next  # 指向下一个结点
        print()
    """
    功能：在头部添加新数据,item是数据
    """

    def add(self, item):
        node = Node(item)  # 添加新数据
        node.next = self.__head  # 新数据的next指向原来的头结点
        self.__head = node  # 新添加的数据变成头结点

    """
    功能：在尾部添加新数据,item是数据
    """

    def append(self, item):
        # 这里的item是一个数据，不是节点
        node = Node(item)  # 新添加数据的结点
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node  # 直接向把新添加信息给头结点
        else:  # 链表不为空
            cur = self.__head  # 初始化cur游标
            while cur.next != None:  # 判断游标指向空，就跳出循环
                cur = cur.next
            cur.next = node  # 指向新添加数据的结点

    """
    功能：在尾部添加新数据,item是数据
    """

    def insert(self, pos, item):

        if pos <= 0:  # 如果pos位置在0或者以前，那么都当做头插法来做
            self.add(item)
        elif pos > self.LinkList_length() - 1:  # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:  # 否则，采用中间位置添加
            node = Node(item)  # 新数据的结点
            count = 0
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node.next = pre.next
            pre.next = node

LinkList_demo = LinkList()#创建链表
LinkList_demo.add(25)#调用add()函数在头结点添加数据
LinkList_demo.add(10)#调用add()函数在头结点添加数据
LinkList_demo.append(39)#调用append()函数在尾结点添加数据
LinkList_demo.insert(2, 49)#调用insert()函数在第3个结点（结点下标从0开始）添加数据
LinkList_demo.insert(4, 54)#调用insert()函数在第5个结点（结点下标从0开始）添加数据
LinkList_demo.insert(0, 60)#调用insert()函数在第1个结点（结点下标从0开始）添加数据
print ("链表的长度是：",LinkList_demo.LinkList_length())#调用LinkList_length()函数输出链表长度
print("链表的各个数据分别是：")
LinkList_demo.LinkList_travel()#调用LinkList_travel()函数输出链表各个数据
