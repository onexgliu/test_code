from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal(18)    # 整数值
b = Decimal(25)
c = Decimal(35)
print(a.remainder_near(10))
print(b.remainder_near(10))
print(c.remainder_near(10))
