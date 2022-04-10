import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal('12')  # 被旋转的数（负数）
y = decimal.Decimal('9')  # 正数
z = decimal.Decimal('-3')  # 负数
k = decimal.Decimal('0')  # 零
result = decimal.getcontext().shift(x, y)
result2 = decimal.getcontext().shift(x, z)
result3 = decimal.getcontext().shift(x, k)
print('x = %s y = %s shift(x,y)结果为：%s' % (x, y, result))
print('x = %s z = %s shift(x,z)结果为：%s' % (x, z, result2))
print('x = %s k = %s shift(x,k)结果为：%s' % (x, k, result3))
