import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
context.prec = 3  # 设置精度为3
x = decimal.Decimal('10.36971')  # 通过字符串创建Decimal对象，值为10.36971
y = decimal.Decimal('-2')  # 通过字符串创建Decimal对象，值为-2
z = decimal.Decimal('0')  # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('Infinity')  # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-Infinity')  # 通过字符串创建Decimal对象，值为-Infinity
print('x = %s 绝对值为：%s' % (x, context.abs(x)))  # 结果为10.4
print('y =%s 绝对值为：%s' % (y, context.abs(y)))  # 结果为2
print('z =%s 绝对值为：%s' % (z, context.abs(z)))  # 结果为0
print('m =%s 绝对值为：%s' % (m, context.abs(m)))  # 结果为Infinity
print('n =%s 绝对值为：%s' % (n, context.abs(n)))  # 结果为Infinity
