from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('0')  # 逻辑操作数0
b = Decimal('1')  # 逻辑操作数1
print(a.logical_or(Decimal('0')))
print(a.logical_or(Decimal('1')))
print(b.logical_or(Decimal('0')))
print(b.logical_or(Decimal('1')))
