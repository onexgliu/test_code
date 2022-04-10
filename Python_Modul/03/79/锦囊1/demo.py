import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
context.prec = 3  # 设置精度为3
x = decimal.Decimal('10')  # 通过字符串创建Decimal对象，值为10
y = decimal.Decimal('2')  # 通过字符串创建Decimal对象，值为2
z = decimal.Decimal('3')  # 通过字符串创建Decimal对象，值为3
k = decimal.Decimal('-5')  # 通过字符串创建Decimal对象，值为-5
m = decimal.Decimal('Infinity')  # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-Infinity')  # 通过字符串创建Decimal对象，值为-Infinity
print('%s/%s = %s' % (x, y, context.divmod(x, y)))  # 结果为(Decimal('5'), Decimal('0'))
print('%s/%s = %s' % (x, z, context.divmod(x, z)))  # 结果为(Decimal('3'), Decimal('1'))
print('%s/%s = %s' % (x, k, context.divmod(x, k)))  # 结果为(Decimal('-2'), Decimal('0'))
print('%s/%s = %s' % (x, m, context.divmod(x, m)))  # 结果为(Decimal('0'), Decimal('10'))
print('%s/%s = %s' % (x, n, context.divmod(x, n)))  # 结果为(Decimal('-0'), Decimal('10'))
