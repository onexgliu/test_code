import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal('1e-9999990')  # 比双精度最小标准正浮点数更小的数
y = decimal.Decimal('-0')  # 通过字符串创建Decimal对象，值为-0
z = decimal.Decimal('NaN')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('-Infinity')  # 通过字符串创建Decimal对象，值为负无穷
print('%s 是否为非正规数：%s' % (x, context.is_subnormal(x)))  # 结果为True
print('%s 是否为非正规数：%s' % (y, context.is_subnormal(y)))  # 结果为False
print('%s 是否为非正规数：%s' % (z, context.is_subnormal(z)))  # 结果为False
print('%s 是否为非正规数：%s' % (k, context.is_subnormal(k)))  # 结果为False
