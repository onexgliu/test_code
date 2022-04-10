def ddSort(theList):                            #定义函数并传入参数theList
    n = 1                                       #子列表长度，初始值为1
    while n < len(theList):
        for i in range(0,len(theList),n*2):
            listA = theList[i:i+n]                       #获取长度为n的左子列表
            listB = theList[i+n:i+n*2]                       #获取长度为n的右子列表
            index = i                                   #定义列表索引
            pointerA = 0                                #定义指针A
            pointerB = 0                                #定义指针B
            while(pointerA<len(listA) and pointerB < len(listB)): #如果两个指针都没走到最后
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
        n = n * 2
sList = [12,9,6,3,1,7,15,10]                     #定义数值列表
print("原数值列表：",sList)                     #打印原数值列表
ddSort(sList)                                   #调用函数
print("排序后的数值列表：",sList)               #打印排序后的数值列表
