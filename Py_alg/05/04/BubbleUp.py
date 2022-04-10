def bubble(data):                             #自定义一个冒泡排序法函数
    for i in range(4,-1,-1):
        for j in range(i):                    #遍历新数据
            if data[j+1]>data[j]:             #如果数据大于原来的数据
                data[j],data[j+1]=data[j+1],data[j]#需要交换位置
        print('第 %d 次排序之后的结果是'%(5-i),end='')#提示
        for j in range(5):                             #遍历每次排序的结果
            print('%4d'%data[j],end='')               #输出结果
        print()                                         #输出空行


data=[14,27,28,4,21]                                   #创建数列并初始化
print("电视台黄金档综艺的收视率如下：")                 #提示
for i in range(5):                                     #遍历原有数据
    print('%4d'%data[i],end='')                       #输出结果
print('\n---------------------------')               #输出分界符
bubble(data)                                            #调用冒泡排序法函数
print('\n---------------------------')           #输出分界符
print("排序之后的综艺的收视率如下：")               #提示
for i in range(5):                                 #遍历排序好的新数列的数据
    print('%4d'%data[i],end='')                   #输出结果
print('')                                           #输出空行
