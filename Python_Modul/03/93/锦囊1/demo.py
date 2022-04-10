import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(0)  # 零
y = decimal.Decimal('-0')  # 通过字符串创建Decimal对象，值为-0
z = decimal.Decimal('NaN')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('0.1')  # 通过字符串创建Decimal对象，值为0.1
print('%s 是否为零：%s' % (x, context.is_zero(x)))  # 结果为True
print('%s 是否为零：%s' % (y, context.is_zero(y)))  # 结果为True
print('%s 是否为零：%s' % (z, context.is_zero(z)))  # 结果为False
print('%s 是否为零：%s' % (k, context.is_zero(k)))  # 结果为False
