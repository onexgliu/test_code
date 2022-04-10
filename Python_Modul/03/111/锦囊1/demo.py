import decimal # 导入十进制定点和浮点运算模块
x = decimal.Decimal('3.1415926') # 正数
y = decimal.Decimal('-0.2000') # 负数
z = decimal.Decimal('0') # 0
result = decimal.getcontext().number_class(x)  # 正数
result2 = decimal.getcontext().number_class(y) # 负数
result3 = decimal.getcontext().number_class(z) # 0
print('x = %s number_class(x)结果为：%s'% (x ,result))
print('y = %s number_class(y)结果为：%s'% (y ,result2))
print('z = %s number_class(z)结果为：%s'% (z ,result3))
