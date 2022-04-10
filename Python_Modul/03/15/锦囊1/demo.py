from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('-1.5')  # 创建Decimal对象a
print(a.compare_total_mag(Decimal('1.0')))
