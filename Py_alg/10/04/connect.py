import sys
import random

"""
功能：将两个职员链表连接
参数：head1:职员1链表头结点
      head2:职员1链表头结点 
"""
def connect_list(head1, head2):
    p = head1#指向头结点为head1的链表
    while p.next != None: #p.next直到为None时,表示head1到了尾结点，跳出循环
        p = p.next#循环指向head1链表的结点
    p.next = head2 #将head1的尾结点链接到head2的头结点上
    return head1


class employee:#创建职员结点
    def __init__(self):
        self.num = 0#职员工位号
        self.salary = 0#职员薪资
        self.name = ''#职员姓名
        self.next = None#指向下一个结点


findword = 0
data = [[None] * 2 for row in range(4)]#列表推导式

employee_data1 = ['张三', '李四', '王五', '刘六']#链表1职员姓名

employee_data2 = ['狗剩', '二狗', '铁蛋', '钢镚']#链表2职员姓名

for i in range(4):#遍历职员
    data[i][0] = i + 1
    data[i][1] = random.randint(5000, 10000)#随机在(5000, 10000)之间生成薪资

head1 = employee()  # 建立第一组链表的头部
if not head1:
    print('Error!! 内存分配失败!!')
    sys.exit(0)

head1.num = data[0][0]#职员1链表头部工位号
head1.name = employee_data1[0]#职员1链表头部姓名
head1.salary = data[0][1]#职员1链表头部薪资
head1.next = None#指向尾结点
p = head1
for i in range(1, 4):  # 建立第一组链表
    newnode = employee()
    newnode.num = data[i][0]#职员1链表工位号
    newnode.name = employee_data1[i]#职员1链表姓名
    newnode.salary = data[i][1]#职员1链表薪资
    newnode.next = None
    p.next = newnode
    p = p.next

for i in range(4):
    data[i][0] = i + 5
    data[i][1] = random.randint(5100, 10000)

head2 = employee()  # 建立第二组链表的头部（和第一组链表一样）
if not head2:
    print('Error!! 内存分配失败!!')
    sys.exit(0)

head2.num = data[0][0]
head2.name = employee_data2[0]
head2.salary = data[0][1]
head2.next = None
p = head2
for i in range(1, 4):  # 建立第二组链表
    new_node = employee()
    new_node.num = data[i][0]
    new_node.name = employee_data2[i]
    new_node.salary = data[i][1]
    new_node.next = None
    p.next = new_node
    p = p.next

i = 0
p = connect_list(head1, head2)  # 调用connect_list()函数将链表相连
print('两个链表相连的结果为：')
while p != None:  # 打印链表的数据
    print("◆",p.num," " *3,p.name," "*3,p.salary,"◇" )
    print()
    p = p.next
