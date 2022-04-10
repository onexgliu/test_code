import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
context.prec = 3  # 设置精度为3
context.rounding = decimal.ROUND_HALF_UP  # 指定四舍五入模式
x = decimal.Decimal('1.5')
y = decimal.Decimal('5E-1')
k = decimal.Decimal('4.5')
z = decimal.Decimal('0.414')
m = decimal.Decimal('0.732')
n = decimal.Decimal(5E+3)
result = decimal.getcontext().to_integral_exact(x)
print('x = %s to_integral_exact(x)结果为：%s' % (x, result))
result2 = context.to_integral_exact(y)
print('y = %s to_integral_exact(y)结果为：%s' % (y, result2))
result3 = context.to_integral_exact(k)
print('k = %s to_integral_exact(k)结果为：%s' % (k, result3))
result4 = context.to_integral_exact(z)
print('z = %s to_integral_exact(z)结果为：%s' % (z, result4))
result5 = context.to_integral_exact(m)
print('m = %s to_integral_exact(m)结果为：%s' % (m, result5))
result6 = context.to_integral_exact(n)
print('n = %s to_integral_exact(n)结果为：%s' % (n, result6))
