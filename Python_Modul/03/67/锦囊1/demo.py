import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('-20') # 通过字符串创建Decimal对象，值为-20
y = decimal.Decimal('-10') # 通过字符串创建Decimal对象，值为-10
z = decimal.Decimal('-0')  # 通过字符串创建Decimal对象，值为-0
k = decimal.Decimal('0')  # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('20.0') # 通过字符串创建Decimal对象，值为20.0
n = decimal.Decimal('20') # 通过字符串创建Decimal对象，值为20
print('%s与%s 的比较结果为：%s'%(x,y,context.compare_signal(x,y)))# 结果为-1
print('%s与%s 的比较结果为：%s'%(x,z,context.compare_signal(x,z)))# 结果为-1
print('%s与%s 的比较结果为：%s'%(z,k,context.compare_signal(z,k)))# 结果为0
print('%s与%s 的比较结果为：%s'%(x,m,context.compare_signal(x,m)))# 结果为-1
print('%s与%s 的比较结果为：%s'%(x,n,context.compare_signal(x,n)))# 结果为-1
print('%s与%s 的比较结果为：%s'%(m,n,context.compare_signal(m,n)))# 结果为0
