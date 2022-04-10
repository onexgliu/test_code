import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('3.14159')  # 被旋转的数（正浮点数）
y = decimal.Decimal('2')  # 正整数
z = decimal.Decimal('-2')  # 负整数
k = decimal.Decimal('0')  # 0
result = decimal.getcontext().subtract(x, y)
result2 = decimal.getcontext().subtract(x, z)
result3 = decimal.getcontext().subtract(x, k)
print('x = %s y = %s subtract(x,y)结果为：%s' % (x, y, result))
print('x = %s z = %s subtract(x,z)结果为：%s' % (x, z, result2))
print('x = %s k = %s subtract(x,k)结果为：%s' % (x, k, result3))
