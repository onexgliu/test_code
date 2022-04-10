from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('0')  # 逻辑操作数0
b = Decimal('1')  # 逻辑操作数1
c = Decimal(0)
d = Decimal(1)
print(a.logical_and(Decimal('0')))
print(b.logical_and(Decimal('1')))
print(c.logical_and(Decimal(0)))
print(d.logical_and(Decimal(1)))
