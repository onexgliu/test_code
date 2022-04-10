import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('-2019')  # 负数
y = decimal.Decimal('4')  # 正数
z = decimal.Decimal('-4')  # 负数
k = decimal.Decimal('2019')  # 正数
m = decimal.Decimal('0')  # 零
result = decimal.getcontext().remainder(x, y)
result2 = decimal.getcontext().remainder(x, z)
result3 = decimal.getcontext().remainder(k, y)
result4 = decimal.getcontext().remainder(k, z)
result5 = decimal.getcontext().remainder(m, y)
print('x = %s y = %s remainder(x,y)结果为：%s' % (x, y, result))
print('x = %s z = %s remainder(x,z)结果为：%s' % (x, z, result2))
print('k = %s y = %s remainder(k,y)结果为：%s' % (k, x, result3))
print('k = %s z = %s remainder(k,z)结果为：%s' % (k, z, result4))
print('m = %s y = %s remainder(m,y)结果为：%s' % (m, y, result5))
