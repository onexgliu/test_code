import random

# 老师名称列表
teachers = ["胡斐", "狄云", "段誉", "郭靖", "韦小宝", "令狐冲", "陈家洛", "杨过", "石中玉", "张无忌"]
while True:
    office_num = input("请输入办公室的个数：")
    least_num = input("请输入每个办公室至少分配老师的个数：")
    if not office_num.isdigit() or not least_num.isdigit():  # 判断输入的是否由数字组成
        print("您的输入有误，请重新输入！")
    elif len(teachers) < int(office_num) * int(least_num):
        print("您的输入有误，请重新输入！")
    else:
        break
office_num = int(office_num)  # 转换为整型
least_num = int(least_num)  # 转换为整型
# 创建办公室列表
offices = []
while office_num >= 1:
    offices.append([])
    office_num -= 1
# 每个办公室随机选出least_num名老师
for i in range(least_num):
    for office in offices:
        index = random.randint(0, len(teachers) - 1)
        # 随机选出一名老师并从老师列表中移除
        teacher = teachers.pop(index)
        office.append(teacher)  # 将选出的老师添加到指定办公室
# 将剩下的老师随机分配
for t in teachers:
    office_index = random.randint(0, len(offices) - 1)
    offices[office_index].append(t)
# 打印老师分配情况
print("分配情况如下：")
for i in range(len(offices)):
    print("第{}个办公室：{}".format(i + 1, "、".join(offices[i])))
