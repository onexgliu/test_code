from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('2.3333333')   # 字符小数值
b = Decimal('nan')         # 空值
print(a.is_nan())
print(b.is_nan())
