import decimal  # 导入十进制定点和浮点运算模块
d = decimal.Decimal('0.7')
print('原：', d)
d2 = decimal.getcontext().copy_decimal(d)  # 复制Decimal对象
d2 = d2 * 100  # 进行乘法运算
print('副本：', d2)
print('原：', d)
