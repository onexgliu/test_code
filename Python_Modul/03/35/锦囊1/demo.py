from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('250')          # 整数
b = Decimal('2.50')         # 浮点
c = Decimal(10)             # 整形参数
print(a.logb())
print(b.logb())
print(c.logb())
