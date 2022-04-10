from decimal import * # 导入十进制定点和浮点运算模块
a = Decimal(1) # 整值
b = Decimal(1.0000) # 浮点值
c = Decimal(1.11) # 浮点值
d = Decimal('NaN') # 空值
print(a.same_quantum(0))
print(b.same_quantum(1))
print(c.same_quantum(0))
print(d.same_quantum(0))
