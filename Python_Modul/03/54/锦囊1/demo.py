from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('1')  # 整值
b = Decimal(1.0000)  # 浮点值
c = Decimal(0)  # 0值
d = Decimal(-1)  # 负值
e = Decimal('NaN')  # 空值
print(a.scaleb(0))
print(b.scaleb(1))
print(c.scaleb(2))
print(d.scaleb(3))
print(d.scaleb(e))
