from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal(1)  # 整值
b = Decimal(0)  # 0值
c = Decimal(-1)  # 负值
d = Decimal('NaN')  # 空值
e = Decimal(1.11)  # 浮点值
print(a.shift(2))
print(b.shift(1))
print(c.shift(-1))
print(d.shift(2))
print(e.shift(2))
print(e.shift(-2))
