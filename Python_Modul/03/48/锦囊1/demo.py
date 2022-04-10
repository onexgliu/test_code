from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal('inf')          # 正无穷值
b = Decimal('-inf')         # 负无穷值
c = Decimal('2.5')          # 正常值
d = Decimal('-2.5')     # 负正常值
e = Decimal('0')            # 0值
f = Decimal('-0')            # -0值
g = Decimal('NaN')          # NaN值
h = Decimal('sNaN')         # sNaN值
print(a.number_class())
print(b.number_class())
print(c.number_class())
print(d.number_class())
print(e.number_class())
print(f.number_class())
print(g.number_class())
print(h.number_class())
