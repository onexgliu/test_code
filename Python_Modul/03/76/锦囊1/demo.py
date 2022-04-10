import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 创建上下文对象
num1 = 3.1415926  # 浮点数
num2 = 1024 # 整数
d2 = context.create_decimal_from_float(num1)  # 创建Decimal对象的实例
print('浮点数：',d2)
d3 = context.create_decimal_from_float(num2)  # 创建Decimal对象的实例
print('整数：',d3)
print('==========更改精度为3后=============')
context.prec = 3  # 设置精度为3
d2 = context.create_decimal_from_float(num1)  # 创建Decimal对象的实例
print('浮点数：',d2)
d3 = context.create_decimal_from_float(num2)  # 创建Decimal对象的实例
print('整数：',d3)
