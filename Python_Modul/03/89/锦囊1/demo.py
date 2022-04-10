import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(0) # 零
y = decimal.Decimal('-nan') # 通过字符串创建Decimal对象，值为-nan
z = decimal.Decimal('nan')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('-9') # 通过字符串创建Decimal对象，值为-9
m = decimal.Decimal('3.14159') # 通过字符串创建Decimal对象，值为3.14159
print('z*x= %s 是否为qNaN：%s'%(z*x,context.is_qnan(z*x)))# 结果为True
print('%s 是否为qNaN：%s'%(y,context.is_qnan(y)))# 结果为True
print('%s 是否为qNaN：%s'%(z,context.is_qnan(z)))# 结果为True
print('%s 是否为qNaN：%s'%(k,context.is_qnan(k)))# 结果为False
print('%s 是否为qNaN：%s'%(m-k,context.is_qnan(m-k)))# 结果为False
