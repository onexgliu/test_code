from decimal import *     # 导入十进制定点和浮点运算模块
a = Decimal('-3.14')       # 创建Decimal实例对象a
print(a.copy_abs())        # 打印Decimal实例对象中参数的绝对值
