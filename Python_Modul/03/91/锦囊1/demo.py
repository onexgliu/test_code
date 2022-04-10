import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(0)  # 0
y = decimal.Decimal('sNaN')  # 通过字符串创建Decimal对象，值为sNaN
z = decimal.Decimal('NaN')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('0.1')  # 通过字符串创建Decimal对象，值为0.1
print('%s 是否为sNaN：%s' % (x, context.is_snan(x)))  # 结果为False
print('%s 是否为sNaN：%s' % (y, context.is_snan(y)))  # 结果为True
print('%s 是否为sNaN：%s' % (z, context.is_snan(z)))  # 结果为False
print('%s 是否为sNaN：%s' % (k, context.is_snan(k)))  # 结果为False
