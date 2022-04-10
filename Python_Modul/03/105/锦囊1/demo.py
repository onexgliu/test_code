import decimal # 导入十进制定点和浮点运算模块
##from decimal import *  # 导入十进制定点和浮点运算模块
x = decimal.Decimal(-100) # 一个数
y = decimal.Decimal('101') # 第二个数
result = decimal.getcontext().minus(x)
result2 = decimal.getcontext().minus(y)
print(result)
print(result2)
