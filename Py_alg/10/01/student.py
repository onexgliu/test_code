"""
功能;创建学生结点类
"""


class student:
    def __init__(self):
        self.name = ''
        self.sex = ''
        self.next = None


head = student()  # 建立链表头部
head.next = None  # 下一个元素为空
ptr = head  # 设存指针的位置
select = 0  # 用来选择
while select != 2:  # 不为2就循环
    print("(1)添加 （2）退出程序")  # 提示
    select = int(input('请输入一个选项：'))
    if select == 1:  # 选择1时,向添加信息
        NewData = student()  # 添加下一个元素
        NewData.no = input("学号：")  # 添加学号
        NewData.name = input("姓名：")  # 添加姓名
        NewData.sex = input("性别：")  # 添加性别
        ptr.next = NewData  # 存指针设置为新元素所在的位置
        NewData.next = None  # 下一个元素的next先设置为空
        ptr = ptr.next  # 指向下一个结点
    elif select == 2:  # 选择2时退出程序
        break
    else:  # 选择其他时，提示有误
        print("输入有误")
