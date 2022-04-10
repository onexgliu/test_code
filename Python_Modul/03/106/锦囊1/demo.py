import decimal # 导入十进制定点和浮点运算模块
##from decimal import *  # 导入十进制定点和浮点运算模块
x = decimal.Decimal(-100) # 一个数
y = decimal.Decimal('1.01') # 第二个数
z = decimal.Decimal('2.00') # 第三个数
a = decimal.Decimal('-2.3')   # 第四个数
result = decimal.getcontext().multiply(x,y)  # 负数乘以正数
result2 = decimal.getcontext().multiply(y,z)  # 正数乘以正数
result3 = decimal.getcontext().multiply(x,a)  # 负数乘以负数
print(result)
print(result2)
print(result3)
