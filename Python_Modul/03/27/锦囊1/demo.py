from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('2.3333333')   # 字符小数值
b = Decimal('nan')         # 空值
c = Decimal('inf')         # 正无穷大的值
d = Decimal('-inf')         # 负无穷大的值
print(a.is_normal())
print(b.is_normal())
print(c.is_normal())
print(d.is_normal())
