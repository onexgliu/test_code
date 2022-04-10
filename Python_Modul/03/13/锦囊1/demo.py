from decimal import *  # 导入十进制定点和浮点运算模块

a = Decimal('-3.14')  # 创建Decimal对象a
b = Decimal('0')  # 创建Decimal对象b
print(a.compare_signal(b))  # 打印比较结果
