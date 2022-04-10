from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal(1)  # 整值
b = Decimal('3')  # 字符值
c = Decimal('NaN')  # 空值
d = Decimal(1.11)  # 浮点值
print(a.sqrt())
print(b.sqrt())
print(c.sqrt())
print(d.sqrt())
