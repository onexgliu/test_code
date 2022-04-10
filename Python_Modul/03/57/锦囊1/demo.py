from decimal import *      # 导入十进制定点和浮点运算模块
a = Decimal(1)       # 整值
b = Decimal('3')     # 字符值
c = Decimal('NaN')     # 空值
d = Decimal(1.11)      # 浮点值
e = Decimal(0.1)
print(a.to_eng_string())
print(b.to_eng_string())
print(c.to_eng_string())
print(d.to_eng_string())
print(e.to_eng_string())
