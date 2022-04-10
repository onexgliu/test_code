import sys
"""
功能：创建链表结点
"""
class student:
    def __init__(self):
        self.number=0#学生学号
        self.name=''#学生姓名
        self.sex = ''#学生性别
        self.next=None#指向下一个结点


"""
功能：删除链表中的结点
"""
def del_ptr(head,ptr):
    top=head#指向链表头结点
    if ptr.number==head.number:  #删除链表头部结点
        head=head.next#取学号
        print('已删除学号 %d 同学 姓名：%s 性别:%s' %(ptr.number,ptr.name,ptr.sex))
    else:
        while top.next!=ptr:  #找到删除节点的前一个位置
            top=top.next
        if ptr.next==None:   #删除链表末尾的结点
            top.next=None
            print('已删除学号 %d 同学 姓名：%s 性别:%s' %(ptr.number,ptr.name,ptr.sex))
        else:
            top.next=ptr.next #删除链表中的任意一个结点
            print('已删除学号 %d 同学 姓名：%s 性别:%s' %(ptr.number,ptr.name,ptr.sex))
    return head  #返回链表


findword=0
name_data=['Luck','Talon','Mark','Bill']#学生姓名
data=[[1,"Woman"],[2,"Man"],[3,"Man"],[4,"Man"]]#学生学号、性别
print('学号 性别 ')
print('-----------')
for i in range(4):#遍历输出链表数据
    for j in range(1):
        print('%2d   %3s  ' %(data[j+i][0],data[j*2+i][1]),end='')
    print()
head=student() #建立链表头部
if not head:
    print('Error!! 内存分配失败!!')
    sys.exit(0)
head.number=data[0][0]#初始化头结点学号
head.name=name_data[0]#初始化头结点姓名
head.sex=data[0][1]#初始化头结点性别
head.next=None
	
ptr=head
for i in range(1,4):  #建立链表
    new_node=student()
    new_node.number=data[i][0]
    new_node.name=name_data[i]
    new_node.sex=data[i][1]
    new_node.number=data[i][0]
    new_node.next=None
    ptr.next=new_node
    ptr=ptr.next
			
while(True):
    findword=int(input('请输入要删除的员工编号,输入0表示结束删除过程,请输入：'))
    if(findword==0): #循环中断条件,输入0程序结束
        break
    else:#否则，根据学号删除学生
        ptr=head
        find=0
        while ptr!=None:
            if ptr.number==findword:#判断学号是否在链表中，是则删除
                ptr=del_ptr(head,ptr)#调用删除函数
                find=find+1
                head=ptr
            ptr=ptr.next
        if find==0:
            print('没有找到')
			
ptr=head
print('\t学号    姓名\t性别')   #打印剩余链表中的数据
print('\t----------------------------')
while(ptr!=None):
    print('\t%2d\t%-5s\t%3s' %(ptr.number,ptr.name,ptr.sex))
    ptr=ptr.next
print('\t----------------------------')
