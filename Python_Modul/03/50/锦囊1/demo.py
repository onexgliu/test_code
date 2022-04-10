from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('1.41421356')  # 浮点值
b = Decimal('1')  # 数值1
c = Decimal('0')  # 数值0
print(a.radix())
print(b.radix())
print(c.radix())
