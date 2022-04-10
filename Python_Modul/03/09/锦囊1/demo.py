from decimal import *  # 导入十进制定点和浮点运算模块

decimal_object = Decimal('-3.14')  # 创建Decimal对象
print(decimal_object.as_integer_ratio())  # 打印对应元祖形式的分数
