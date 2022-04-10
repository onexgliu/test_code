from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('inf')  # 正无穷大的值
b = Decimal('-inf')  # 负无穷大的值
c = Decimal('nan')  # 空值
d = Decimal('2.3333333')  # 字符小数值
print(a.is_infinite())
print(b.is_infinite())
print(c.is_infinite())
print(d.is_infinite())
