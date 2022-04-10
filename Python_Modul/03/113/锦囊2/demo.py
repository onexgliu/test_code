import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 3  # 设置精度为3
x = decimal.Decimal('2')  # 正数
y = decimal.Decimal('20')  # 正数
z = decimal.Decimal('0')  # 零
k = decimal.Decimal('200')  # 正数
result = decimal.getcontext().power(x, y, k)
result2 = decimal.getcontext().power(y, z, x)
result3 = decimal.getcontext().power(y, x, k)
print('x = %s y = %s k = %s power(x,y,k)结果为：%s' % (x, y, k, result))
print('y = %s z = %s x = %s power(y,z,x)结果为：%s' % (y, z, x, result2))
print('y = %s x = %s k = %s power(y,x,k)结果为：%s' % (y, x, k, result3))
