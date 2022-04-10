"""
功能：定义职员队列链表

"""
class worker:
    def __init__(self):
        self.name=''*20#职员名字
        self.number=0#职员工位号
        self.next=None#队列中指向下一个结点
fore=worker()
end=worker()
fore=None#队列前端指针
end=None#队列末尾指针
"""
功能：将数据加入到队列
参数：name：表示职员名字
      number:表示职员工位号
"""
def add_queue(name,number):
    global fore
    global end
    new_data=worker()#分配内存给新数据
    new_data.name=name#为新数据赋值
    new_data.number=number#为新数据赋值
    if end==None:#如果end为None,表示这是第一个元素
        fore=new_data
    else:
        end.next=new_data#将新数据连接到队列末尾
    end=new_data#将end指向新数据，这是新数据的末尾
    new_data.next=None#新数据之后再无其他数据
"""
功能：取出队列数据
"""
def out_queue():
    global fore
    global end
    if fore==None:#如果队列前端为None，表示这个队列为空
        print("队列已经没有数据了")
    else:#否则
        print("姓名：",fore.name," 工号：",fore.number)#输出信息
        fore=fore.next #将队列前端移到下一个元素
"""
功能：显示队列中的数据
"""
def show():
    global fore
    global end
    p = fore#从队列前端开始
    if p== None:#判断p为空，则队列为空
        print('队列已空！')#提示
    else:
        while p != None:  # 从队列前端(fore)到队列末尾(end)遍历队列
            print("姓名：",p.name,"\t工号:", p.number)#输出队列信息
            p = p.next#指向下一个结点


i = 0#用于选择变量
while True:
    i = int(input("1:向队列加入数据 2:从队列中取出数据 3:显示队列中数据 4:退出程序,请选择："))#提示
    if i == 1:#选择1
        name = input("姓名: ")#输出职员姓名
        score = int(input("工位号: "))#输入职员工位号
        add_queue(name, score)#向队列中加入数据
    elif i == 2:#选择2
        out_queue()#在队列中取出数据
    elif i==3:#选择3
        show()#显示在队列中未取出的数据
    elif i == 4:#选择4
            break#退出程序
    else:#否则
        print("输入有误")#提示输入有误

