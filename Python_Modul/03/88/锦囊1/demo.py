import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal('-Inf') # 通过字符串创建Decimal对象，值为负无穷
y = decimal.Decimal('nan') # 通过字符串创建Decimal对象，值为NaN
z = decimal.Decimal('-nan')  # 通过字符串创建Decimal对象，值为-NaN
k = decimal.Decimal('0') # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('3.14159') # 通过字符串创建Decimal对象，值为3.14159
print('%s 是否为正常数：%s'%(x,context.is_normal(x)))# 结果为False
print('%s 是否为正常数：%s'%(y,context.is_normal(y)))# 结果为False
print('%s 是否为正常数：%s'%(z,context.is_normal(z)))# 结果为False
print('%s 是否为正常数：%s'%(k,context.is_normal(k)))# 结果为False
print('m-k = %s 是否为正常数：%s'%(m-k,context.is_normal(m-k)))# 结果为True
