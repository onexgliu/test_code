from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal.from_float(0.1)  # 浮点值
b = Decimal.from_float(float('nan'))  # 空值
c = Decimal.from_float(float('inf'))  # 正无穷值
d = Decimal.from_float(float('-inf'))  # 负无穷值
print(a)
print(b)
print(c)
print(d)
