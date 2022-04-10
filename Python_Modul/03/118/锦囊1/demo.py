import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('-2019')  # 被旋转的数（负数）
y = decimal.Decimal('3')  # 顺时针旋转
z = decimal.Decimal('-3')  # 逆时针旋转
k = decimal.Decimal('2019')  # 被旋转的数（正数）
result = decimal.getcontext().rotate(x, y)  # 顺时针旋转
result2 = decimal.getcontext().rotate(x, z)  # 逆时针旋转
result3 = decimal.getcontext().rotate(k, y)  # 顺时针旋转
result4 = decimal.getcontext().rotate(k, z)  # 逆时针旋转
print('x = %s y = %s rotate(x,y)结果为：%s' % (x, y, result))
print('x = %s z = %s rotate(x,z)结果为：%s' % (x, z, result2))
print('k = %s y = %s rotate(k,y)结果为：%s' % (k, y, result3))
print('k = %s z = %s rotate(k,z)结果为：%s' % (k, z, result4))
