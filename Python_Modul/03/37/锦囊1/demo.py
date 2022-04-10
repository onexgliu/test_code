from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('0')            # 操作数0
b = Decimal('1')            # 操作数1
c = Decimal('111111111')
d = Decimal('101010101')
print(a.logical_invert())
print(b.logical_invert())
print(c.logical_invert())
print(d.logical_invert())
