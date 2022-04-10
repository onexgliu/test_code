import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
####context.prec = 8 # 设置精度为8
x = decimal.Decimal('-Inf') # 通过字符串创建Decimal对象，值为负无穷
y = decimal.Decimal('nan') # 通过字符串创建Decimal对象，值为nan
z = decimal.Decimal('Inf')  # 通过字符串创建Decimal对象，值为正无穷
k = decimal.Decimal('0') # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('1.1E+1000') # 通过字符串创建Decimal对象，值为3.14159
print('%s 是否为正负无穷大：%s'%(x,context.is_infinite(x)))# 结果为True
print('%s 是否为正负无穷大：%s'%(y,context.is_infinite(y)))# 结果为False
print('%s 是否为正负无穷大：%s'%(z,context.is_infinite(z)))# 结果为True
print('%s 是否为正负无穷大：%s'%(k,context.is_infinite(k)))# 结果为False
print('m-k = %s 是否为正负无穷大：%s'%(m-k,context.is_infinite(m-k)))# 结果为False
