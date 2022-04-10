from decimal import *  # 导入十进制定点和浮点运算模块

print(Decimal(7))  # 传递整型参数
print(Decimal('0.1'))  # 传递字符串类型参数
print(Decimal(0.1))  # 传递浮点类型参数
print(Decimal((1, (1, 7, 3, 2), -3)))  # 传递元组类型参数

import decimal  # 导入十进制定点和浮点运算模块

print(decimal.Decimal(7))  # 传递整型参数
print(decimal.Decimal('0.1'))  # 传递字符串类型参数
print(decimal.Decimal(0.1))  # 传递浮点类型参数
print(decimal.Decimal((1, (1, 7, 3, 2), -3)))  # 传递元组类型参数
