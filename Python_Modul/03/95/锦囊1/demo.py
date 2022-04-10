import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal(0)  # 零
y = decimal.Decimal(100)  # 整数
z = decimal.Decimal('0.001')  # 通过字符串创建Decimal对象，值为0.001
print(decimal.getcontext().log10(x))  # 结果为-Infinity
print(decimal.getcontext().log10(y))  # 结果为2
print(decimal.getcontext().log10(z))  # 结果为-3
