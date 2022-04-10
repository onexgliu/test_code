import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 3  # 设置精度为3
x = decimal.Decimal('0.1')  # 一个数
y = decimal.Decimal('0.2')  # 第二个数
z = decimal.Decimal('-0.1')  # 第三个数
k = decimal.Decimal('-0.2')  # 第三个数
result = decimal.getcontext().next_toward(x, y)  # 两个正数
result2 = decimal.getcontext().next_toward(z, y)  # 一正一负
result3 = decimal.getcontext().next_toward(z, k)  # 两个负数
print('x = %s y = %s next_toward(x,y)结果为：%s' % (x, y, result))
print('z = %s y = %s next_toward(z,y)结果为：%s' % (z, y, result2))
print('z = %s k = %s next_toward(z,k)结果为：%s' % (z, k, result3))
