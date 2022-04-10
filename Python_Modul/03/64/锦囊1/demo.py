import decimal # 导入十进制定点和浮点运算模块
x = decimal.Decimal('0.1') # 一个数
result = decimal.getcontext().canonical(x)  # 返回相同的Decimal对象
print(result)
