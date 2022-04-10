from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('-nan')         # 带负号空值
b = Decimal('-inf')         # 负无穷大的值
c=  Decimal('-0')           # 负0值
print(a.is_signed())
print(b.is_signed())
print(c.is_signed())
