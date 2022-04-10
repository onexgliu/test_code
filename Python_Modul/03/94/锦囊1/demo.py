import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 8 # 设置精度为8
x = decimal.Decimal(0) # 零
y = decimal.Decimal(100) # 整数
z = decimal.Decimal('0.001')  # 通过字符串创建Decimal对象，值为0.001
print(context.ln(x))# 结果为-Infinity
print(context.ln(y))# 结果为4.6051702
print(context.ln(z))# 结果为-6.9077553
