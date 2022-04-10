from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('1.2000')  # 浮点多0值
b = Decimal('1.000')
c = Decimal('0.0')
d = Decimal('-120.00')
print(a.normalize())
print(b.normalize())
print(c.normalize())
print(d.normalize())
