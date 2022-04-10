from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('1.2')  # 创建Decimal对象a
print(a.compare_total(Decimal('NaN')))
print(a.compare_total(Decimal('1.0')))
print(a.compare_total(Decimal('1.5')))
print(a.compare_total(Decimal('inf')))
print(a.compare_total(Decimal('1.20')))
