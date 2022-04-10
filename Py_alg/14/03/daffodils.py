import math    #导入数学模块

print('100~1000之间的水仙花数有：')
for num in range(100, 1000):#循环遍历100~1000之间的数
    a = num           #num保存最后的水仙花数
    hundred = a // 100#取整数的百位
    a = a - hundred * 100 #取整数的十位
    ten = a // 10
    single = a % 10#取整数的个位；
    a = pow(hundred, 3)#百位的3次幂
    b = pow(ten, 3)#十位的3次幂
    c = pow(single, 3)#个位的3次幂    
    if a + b +c == num:#判断求得的a+b+c的值是否等于水仙花数      
        print(num)#是，则输出num的值
