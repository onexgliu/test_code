def dgSort(theList):                            #定义函数并传入参数theList
    if len(theList) < 2:                        #如果theList只有一个元素
        return                                  #终止程序执行
    sep = len(theList) // 2                     #将列表一分为二
    listA = theList[:sep]                       #获取左子列表
    listB = theList[sep:]                       #获取右子列表
    dgSort(listA)                               #对左子列表进行递归排序
    dgSort(listB)                               #对右子列表进行递归排序
    index = 0                                   #定义列表索引
    pointerA = 0                                #定义指针A
    pointerB = 0                                #定义指针B
    while(pointerA<len(listA) and pointerB < len(listB)):   #如果两个指针都没走到最后
        if(listA[pointerA] < listB[pointerB]):  #比较指针指向的两个元素大小
            theList[index] = listA[pointerA]    #把较小的元素作为当前索引的元素
            pointerA += 1                       #向后移动指针A
        else:
            theList[index] = listB[pointerB]    #把较大的元素作为当前索引的元素
            pointerB += 1                       #向后移动指针B
        index += 1                              #当前索引加1
    while(pointerA < len(listA)):               #如果指针B走到最后而指针A没有
        theList[index] = listA[pointerA]        #把指针A指向的元素作为当前索引的元素
        pointerA += 1                           #向后移动指针A
        index += 1                              #当前索引加1
    while (pointerB < len(listB)):              #如果指针A走到最后而指针B没有
        theList[index] = listB[pointerB]        #把指针B指向的元素作为当前索引的元素
        pointerB += 1                           #向后移动指针B
        index += 1                              #当前索引加1
sList = [2,-2,5,3,-3,0,9,6]                     #定义数值列表
print("原数值列表：",sList)
dgSort(sList)                                   #调用函数
print("排序后的数值列表：",sList)               #打印排序后的列表