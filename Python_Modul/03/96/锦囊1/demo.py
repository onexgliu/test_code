import decimal # 导入十进制定点和浮点运算模块
x = decimal.Decimal(0.14159) # 小数
y = decimal.Decimal(-300) # 负整数
z = decimal.Decimal('1001')  # 通过字符串创建Decimal对象，值为1001
print(decimal.getcontext().logb(x))# 结果为-1
print(decimal.getcontext().logb(y))# 结果为2
print(decimal.getcontext().logb(z))# 结果为3
