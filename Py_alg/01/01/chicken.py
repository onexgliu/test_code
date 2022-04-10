
for i in range(1,20):                                       #遍历公鸡个数
    for j in range(1,33):                                   #遍历母鸡个数
        for k in range(3,99,3):                             #遍历雏鸡个数
            if i+j+k==100 and 5*i + 3*j + k//3 ==100:       #百钱百鸡条件
                print("公鸡：",i,"母鸡：",j,"雏鸡：",k)     #输出结果
