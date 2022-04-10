import decimal  # 导入十进制定点和浮点运算模块

##from decimal import *  # 导入十进制定点和浮点运算模块
decimal.getcontext().prec = 3  # 设置精度为3
x = decimal.Decimal('3.1415926')  # 超出指定精度的小数，并且截取后以0结尾
y = decimal.Decimal('0.2000')  # 以0结尾的小数
z = decimal.Decimal('0.10001')  # 超出指定精度的小数
k = decimal.Decimal('02019')  # 超出精度的整数
result = decimal.getcontext().normalize(x)  # 超出指定精度的小数，并且截取后以0结尾
result2 = decimal.getcontext().normalize(y)  # 以0结尾的小数
result3 = decimal.getcontext().normalize(z)  # 超出指定精度的小数
result4 = decimal.getcontext().normalize(k)  # 超出指定精度的整数
print('x = %s normalize(x)结果为：%s' % (x, result))
print('y = %s normalize(y)结果为：%s' % (y, result2))
print('z = %s normalize(z)结果为：%s' % (z, result3))
print('k = %s normalize(z)结果为：%s' % (k, result4))
