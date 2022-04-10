import decimal # 导入十进制定点和浮点运算模块
x = decimal.Decimal(131) # 一个正数
y = decimal.Decimal('-1500') # 一个负数
z = decimal.Decimal('0') # 零
result = decimal.getcontext().min(x,y)  # 输出-1500
result2 = decimal.getcontext().min(x,z)  # 输出0
result3 = decimal.getcontext().min(y,z)  # 输出-1500
print(result)
print(result2)
print(result3)
