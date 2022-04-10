from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('0')  # 操作数0
b = Decimal('1')  # 操作数1
print(a.max(Decimal('-inf')))
print(a.max(Decimal('1')))
print(b.max(Decimal('3.21')))
print(b.max(Decimal('-3.21')))
