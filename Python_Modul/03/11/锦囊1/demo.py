from decimal import *  # 导入十进制定点和浮点运算模块

decimal_object = Decimal('-3.14')  # 创建Decimal对象
print(decimal_object.canonical())  # 打印Decimal对象中的参数
