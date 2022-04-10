from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('0')                # 参数为0
b = Decimal('0.001')            # 参数为浮点数
c = Decimal('2')                # 参数为整数
d = Decimal('inf')              # 正无穷大的值
print(a.log10())
print(b.log10())
print(c.log10())
print(d.log10())
