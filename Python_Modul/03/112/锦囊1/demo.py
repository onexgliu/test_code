import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 3  # 设置精度为3
x = decimal.Decimal('3.1415926')  # 正浮点数
y = decimal.Decimal('-0.2000')  # 负浮点数
z = decimal.Decimal('202')  # 正整数
result = decimal.getcontext().plus(x)  # 正数
result2 = decimal.getcontext().plus(y)  # 负数
result3 = decimal.getcontext().plus(z)  # 正整数
print('x = %s plus(x)结果为：%s' % (x, result))
print('y = %s plus(y)结果为：%s' % (y, result2))
print('z = %s plus(z)结果为：%s' % (z, result3))
