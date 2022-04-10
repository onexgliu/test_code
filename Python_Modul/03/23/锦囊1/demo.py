from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('2.3').fma(3,5)   # 指定字符小数值，计算过程2.3*3+5
b = Decimal(2.3).fma(3,5)     # 指定小数值，计算过程2.2999999999999998223...*3+5
c = Decimal(3).fma(3,5)       # 指定整数值，计算过程3*3+5
print(a.is_canonical())
print(b.is_canonical())
print(c.is_canonical())
