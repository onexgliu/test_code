import sys
"""
功能：创建链表结点
"""
class student:
    def __init__(self):
        self.number=0
        self.name=''
        self.sex = ''
        self.next=''

findword=0

name_data=['Luck','Talon','Mark','Bill']#链表学生名字

data=[[1,"Woman"],[2,"Man"],[3,"Man"],[4,"Man"]]#链表学生学号和性别

head=student() #建立链表头部
if not head:
    print('Error!! 内存分配失败!!')
    sys.exit(0)

head.number=data[0][0]#链表头部学生学号
head.name=name_data[0]#链表头部学生姓名
head.sex=data[0][1]#链表头部学生性别
head.next=None
ptr=head
for i in range(1,4): #建立链表
    new_node=student()
    new_node.number=data[i][0]#初始化链表学生学号
    new_node.name=name_data[i]#初始化链表学生姓名
    new_node.sex=data[i][1]#初始化链表学生性别
    new_node.next=None
    ptr.next=new_node#指向学生链表下一个结点
    ptr=ptr.next

ptr=head
i=0
print('反转前的学生链表节点数据：')
while ptr !=None:  #打印链表数据
    print('☆ %2d\t  %-1s\t%-3s  ☆' %(ptr.number,ptr.name,ptr.sex), end='')
    i=i+1
    if i>=1: #一个数据为一行
        print()
        i=0
    ptr=ptr.next#指向下一个结点

ptr=head
before=None   
print('\n反转后的学生链表节点数据：')
while ptr!=None: #链表反转,利用三个指针，反转指针核心
    last=before
    before=ptr
    ptr=ptr.next
    before.next=last

ptr=before
while ptr!=None: #打印链表数据
    print('★ %2d\t  %-1s\t%-3s   ★' %(ptr.number,ptr.name,ptr.sex), end='')
    i=i+1
    if i>=1:#一个数据为一行
        print()
        i=0
    ptr=ptr.next
