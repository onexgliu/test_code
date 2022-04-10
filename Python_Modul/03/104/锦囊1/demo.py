import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal(131)  # 一个正数
y = decimal.Decimal('-1500')  # 一个负数
z = decimal.Decimal('0')  # 零
result = decimal.getcontext().min_mag(x, y)  # 输出131
result2 = decimal.getcontext().min_mag(x, z)  # 输出0
result3 = decimal.getcontext().min_mag(y, z)  # 输出0
print(result)
print(result2)
print(result3)
