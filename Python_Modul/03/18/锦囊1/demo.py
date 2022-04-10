from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('-1.2')  # 创建Decimal对象a
b = Decimal('1.2')  # 创建Decimal对象a
c = Decimal(3.1415926)  # 创建Decimal对象c
d = Decimal(-3.1415926)  # 创建Decimal对象d
print(a.copy_negate())
print(b.copy_negate())
print(c.copy_negate())
print(d.copy_negate())
