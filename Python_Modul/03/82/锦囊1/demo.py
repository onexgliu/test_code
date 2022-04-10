import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
context.prec = 3  # 设置精度为3
x = decimal.Decimal('1')  # 通过字符串创建Decimal对象，值为1
y = decimal.Decimal('2')  # 通过字符串创建Decimal对象，值为2
z = decimal.Decimal('-Infinity')  # 通过字符串创建Decimal对象，值为负无穷
k = decimal.Decimal('0')  # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('Infinity')  # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-1')  # 通过字符串创建Decimal对象，值为-1
print('x=%s %s' % (x, context.exp(x)))  # 结果为2.72
print('y=%s %s' % (y, context.exp(y)))  # 结果为7.39
print('z=%s %s' % (z, context.exp(z)))  # 结果为0
print('k=%s %s' % (k, context.exp(k)))  # 结果为1
print('m=%s %s' % (m, context.exp(m)))  # 结果为Infinity
print('n=%s %s' % (n, context.exp(n)))  # 结果为0.368
