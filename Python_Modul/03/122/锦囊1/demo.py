import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal('4')
y = decimal.Decimal('2')
z = decimal.Decimal('4.6')
k = decimal.Decimal('0')
result = decimal.getcontext().sqrt(x)
result2 = decimal.getcontext().sqrt(y)
result3 = decimal.getcontext().sqrt(z)
result4 = decimal.getcontext().sqrt(k)
print('x = %s sqrt(x)结果为：%s' % (x, result))
print('y = %s sqrt(y)结果为：%s' % (y, result2))
print('z = %s sqrt(z)结果为：%s' % (z, result3))
print('k = %s sqrt(k)结果为：%s' % (k, result4))
