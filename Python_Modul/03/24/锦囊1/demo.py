from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('inf')         # 无穷大的值
b = Decimal('nan')         # 空值
c = Decimal('2.3333333')   # 字符小数值
d = Decimal(3.1415926)     # 小数值
print(a.is_finite())
print(b.is_finite())
print(c.is_finite())
print(d.is_finite())
