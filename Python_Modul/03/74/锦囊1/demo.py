import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('10') # 通过字符串创建Decimal对象，值为10
y = decimal.Decimal('-2') # 通过字符串创建Decimal对象，值为-2
z = decimal.Decimal('0')  # 通过字符串创建Decimal对象，值为0
m = decimal.Decimal('Infinity') # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-Infinity') # 通过字符串创建Decimal对象，值为-Infinity
print('x = %s y =%s 结果为：%s'%(x,y,context.copy_sign(x,y)))# 结果为-10
print('y = %s x =%s 结果为：%s'%(y,x,context.copy_sign(y,x)))# 结果为2
print('x = %s z =%s 结果为：%s'%(x,z,context.copy_sign(x,z)))# 结果为10
print('x = %s m =%s 结果为：%s'%(x,m,context.copy_sign(x,m)))# 结果为10
print('x = %s n =%s 结果为：%s'%(x,n,context.copy_sign(x,n)))# 结果为-10
