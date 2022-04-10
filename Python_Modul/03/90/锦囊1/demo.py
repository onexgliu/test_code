import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(0) # 零
y = decimal.Decimal('-0') # 通过字符串创建Decimal对象，值为-0
z = decimal.Decimal('NaN')  # 通过字符串创建Decimal对象，值为NaN
k = decimal.Decimal('-9') # 通过字符串创建Decimal对象，值为-9
m = decimal.Decimal('3.14159') # 通过字符串创建Decimal对象，值为3.14159
print('%s 是否为负数：%s'%(x,context.is_signed(x)))# 结果为False
print('%s 是否为负数：%s'%(y,context.is_signed(y)))# 结果为True
print('%s 是否为负数：%s'%(z,context.is_signed(z)))# 结果为False
print('%s 是否为负数：%s'%(k,context.is_signed(k)))# 结果为True
print('%s 是否为负数：%s'%(m-k,context.is_signed(m-k)))# 结果为False
