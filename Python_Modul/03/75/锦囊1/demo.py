import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 创建上下文对象
context.prec = 3  # 设置精度为3
d = decimal.Decimal('3.1415926')
print('原：',d)
d2 = context.create_decimal(d)  # 创建Decimal对象的实例
print('新：',d2)
d2 = d2*100  # 进行乘法运算
print('新（运算后）：',d2)
print('原：',d)
print('==========更改精度为5后=============')
context.prec = 5  # 设置精度为5
d2 = context.create_decimal(d)  # 创建Decimal对象的实例
print('新：',d2)
d2 = d2*100  # 进行乘法运算
print('新（运算后）：',d2)
print('原：',d)
