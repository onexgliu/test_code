from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('0')            # 操作数0
b = Decimal('1')            # 操作数1
print(a.min_mag(Decimal('-inf')))
print(a.min_mag(Decimal('1')))
print(b.min_mag(Decimal('3.21')))
print(b.min_mag(Decimal('-3.21')))
