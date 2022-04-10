from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('0')  # 逻辑操作数0
b = Decimal('1')  # 逻辑操作数1
c = Decimal('inf')  # 无穷大
d = Decimal('NaN')  # 空值
print(a.next_minus())
print(b.next_minus())
print(c.next_minus())
print(d.next_minus())
