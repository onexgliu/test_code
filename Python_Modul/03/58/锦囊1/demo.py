from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal(7E+3)  # 7000值
b = Decimal(5E-3)  # 0.005....
c = Decimal(1.5)
d = Decimal(0.5)
print(a.to_integral_exact())
print(b.to_integral_exact())
print(c.to_integral_exact())
print(d.to_integral_exact())
