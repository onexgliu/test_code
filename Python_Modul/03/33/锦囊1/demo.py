from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('0')  # 参数为0
b = Decimal('-0')  # 参数为-0
c = Decimal('nan')  # 参数为空
d = Decimal('2.50')  # 小数值
print(a.ln())
print(b.ln())
print(c.ln())
print(d.ln())
