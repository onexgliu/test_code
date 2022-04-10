from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('-nan')  # 带负号空值
b = Decimal('2.50')  # 小数值
c = Decimal('sNaN')  # 信号NaN
print(a.is_snan())
print(b.is_snan())
print(c.is_snan())
