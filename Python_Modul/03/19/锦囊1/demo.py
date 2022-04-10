from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('-3.14')       # 创建Decimal实例对象a
b = Decimal('2.16')        # 创建Decimal实例对象b
print(a.copy_sign(b))        # 打印Decimal实例对象a的副本，由于第二操作数b为正数所以副本为正数
