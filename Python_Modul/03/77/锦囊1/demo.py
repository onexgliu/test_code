import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('10') # 通过字符串创建Decimal对象，值为10
y = decimal.Decimal('2') # 通过字符串创建Decimal对象，值为2
z = decimal.Decimal('3')  # 通过字符串创建Decimal对象，值为3
k = decimal.Decimal('-5') # 通过字符串创建Decimal对象，值为-5
m = decimal.Decimal('Infinity') # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-Infinity') # 通过字符串创建Decimal对象，值为-Infinity
print('%s/%s = %s'%(x,y,context.divide(x,y)))# 结果为5
print('%s/%s = %s'%(x,z,context.divide(x,z)))# 结果为3.33
print('%s/%s = %s'%(x,k,context.divide(x,k)))# 结果为-2
print('%s/%s = %s'%(x,m,context.divide(x,m)))# 结果为0E-1000001
print('%s/%s = %s'%(x,n,context.divide(x,n)))# 结果为-0E-1000001
