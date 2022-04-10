import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal('6') # 通过字符串创建Decimal对象，值为6
y = decimal.Decimal('9') # 通过字符串创建Decimal对象，值为9
z = decimal.Decimal('Inf')  # 通过字符串创建Decimal对象，值为正无穷
k = decimal.Decimal('-10') # 通过字符串创建Decimal对象，值为-10
m = decimal.Decimal('1.1E+10') # 通过字符串创建Decimal对象，值为1.1E+10
print('%s*%s+%s=%s'%(x,y,z,context.fma(x,y,z)))# 结果为Infinity
print('%s*%s+(%s)=%s'%(x,y,k,context.fma(x,y,k)))# 结果为44
print('%s*%s+(%s)=%s'%(x,m,k,context.fma(x,m,k)))# 结果为65999999990
