import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
context.prec = 8  # 设置精度为8
x = decimal.Decimal(11)  # 值为11的二进制数
y = decimal.Decimal(0)  # 值为0的二进制数
z = decimal.Decimal('10010')  # 值为10010的二进制数
print(x, '反转后：', context.logical_invert(x))
print(y, '反转后：', context.logical_invert(y))
print(z, '反转后：', context.logical_invert(z))
