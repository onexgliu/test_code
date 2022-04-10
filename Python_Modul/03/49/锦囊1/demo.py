from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('1.41421356')          # 浮点值
print(a.quantize(Decimal('1.000')))
