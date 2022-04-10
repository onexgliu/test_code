import decimal  # 导入十进制定点和浮点运算模块
x = decimal.Decimal(-100)  # 一个数
y = decimal.Decimal('1.01')  # 第二个数
z = decimal.Decimal('-2.3')  # 第三个数
a = decimal.Decimal(2000)  # 第四个数
result = decimal.getcontext().next_plus(x)  # 负整数
result2 = decimal.getcontext().next_plus(y)  # 正小数
result3 = decimal.getcontext().next_plus(z)  # 负数小数
result4 = decimal.getcontext().next_plus(a)  # 正整数
print('大于', x, '的最小数是', result)
print('大于', y, '的最小数是', result2)
print('大于', z, '的最小数是', result3)
print('大于', a, '的最小数是', result4)
