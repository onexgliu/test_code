from decimal import *  # 导入十进制定点和浮点运算模块
decimal_object = Decimal('321e+5')    # 创建Decimal对象
print(decimal_object)                 # 打印对象结果
print(decimal_object.adjusted())      # 打印用于确定最高有效位相对于小数点的位置
