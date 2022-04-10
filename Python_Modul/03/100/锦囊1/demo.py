import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal(1)  # 一个数
y = decimal.Decimal(0)  # 第二个数
z = decimal.Decimal('01')  # 第三个数（创建为Decimal对象后值为1）
result = decimal.getcontext().logical_xor(x, y)  # 1和0进行逻辑异或运算，结果为1
result2 = decimal.getcontext().logical_xor(x, z)  # 1和1进行逻辑异或运算，结果为0
print(result)
print(result2)
