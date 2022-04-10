import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('3.14159')  # 正数
y = decimal.Decimal('0.01')  # 两位小数
z = decimal.Decimal('0')  # 零
k = decimal.Decimal('1e-1')  # 0.1
m = decimal.Decimal('Infinity')  # 正无穷
result = decimal.getcontext().quantize(x, y)
result2 = decimal.getcontext().quantize(x, z)
result3 = decimal.getcontext().quantize(x, k)
result4 = decimal.getcontext().quantize(decimal.Decimal('-Inf'), decimal.Decimal('Infinity'))
print('x = %s y = %s quantize(x,y)结果为：%s' % (x, y, result))
print('x = %s z = %s quantize(x,z)结果为：%s' % (x, z, result2))
print('x = %s k = %s quantize(x,k)结果为：%s' % (x, k, result3))
print('quantize(decimal.Decimal(\'-Inf\'),decimal.Decimal(\'Infinity\'))结果为：%s' % (result4))
