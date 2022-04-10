from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal(1)  # 整值
b = Decimal(1.0000)  # 浮点值
print(a.rotate(1))  # 向左旋转1位
print(b.rotate(3))  # 向左旋转3位
