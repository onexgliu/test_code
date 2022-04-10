import decimal  # 导入十进制定点和浮点运算模块
x = decimal.Decimal(-100)  # 一个数
y = decimal.Decimal('1.01')  # 第二个数
z = decimal.Decimal('-2.3')  # 第三个数
a = decimal.Decimal(2000)  # 第四个数
result = decimal.getcontext().next_minus(x)  # 负整数
result2 = decimal.getcontext().next_minus(y)  # 正小数
result3 = decimal.getcontext().next_minus(z)  # 负数小数
result4 = decimal.getcontext().next_minus(a)  # 正整数
print('小于', x, '的最大数是', result)
print('小于', y, '的最大数是', result2)
print('小于', z, '的最大数是', result3)
print('小于', a, '的最大数是', result4)
