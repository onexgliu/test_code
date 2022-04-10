import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(0) # 零
y = decimal.Decimal('nan') # 通过字符串创建Decimal对象，值为qnan
z = decimal.Decimal('-nan')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('-9') # 通过字符串创建Decimal对象，值为-9
m = decimal.Decimal('3.14159') # 通过字符串创建Decimal对象，值为3.14159
print('z*x= %s 是否为NaN：%s'%(z*x,context.is_nan(z*x)))# 结果为True
print('%s 是否为NaN：%s'%(y,context.is_nan(y)))# 结果为True
print('%s 是否为NaN：%s'%(z,context.is_nan(z)))# 结果为True
print('%s 是否为NaN：%s'%(k,context.is_nan(k)))# 结果为False
print('m-k = %s 是否为NaN：%s'%(m-k,context.is_nan(m-k)))# 结果为False
