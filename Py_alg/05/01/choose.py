def choose(data):                                     #自定义一个选择排序法函数
    for i in range(4):                                #遍历新数据
        for j in range(i+1,5):                        #遍历新数据
            if data[j]<data[i]:                       #如果数据小于原来的数据
                data[i],data[j]=data[j],data[i]       #需要交换位置
        print('第 %d 次排序之后的结果是'%(i+1),end='')#提示
        for j in range(5):                            #遍历每次排序的结果
            print('%3d'%data[j],end='')               #输出结果
        print()                                       #输出空行


data=[56,18,49,84,72]                                  #创建数列并初始化
print("原始数据为：")                                  #提示
for i in range(5):                                     #遍历原有数据
    print('%3d'%data[i],end='')                        #输出结果
print('\n---------------------------')                 #输出分界符
choose(data)                                           #调用选择排序法函数
print('\n---------------------------')                 #输出分界符
print("排序之后的数据为：")                            #提示
for i in range(5):                                     #遍历排序好的新数列的数据
    print('%3d'%data[i],end='')                        #输出结果
print('')                                              #输出空行
