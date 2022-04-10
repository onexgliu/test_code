from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('nan')         # 静默空值
b = Decimal()              # 非静默空值
print(a.is_qnan())
print(b.is_qnan())
