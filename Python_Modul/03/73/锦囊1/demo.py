import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('10') # 通过字符串创建Decimal对象，值为10
y = decimal.Decimal('-2') # 通过字符串创建Decimal对象，值为2
z = decimal.Decimal('0')  # 通过字符串创建Decimal对象，值为3
m = decimal.Decimal('Infinity') # 通过字符串创建Decimal对象，值为Infinity
n = decimal.Decimal('-Infinity') # 通过字符串创建Decimal对象，值为-Infinity
print('x = %s 符号反转后：%s'%(x,context.copy_negate(x)))# 结果为-10
print('y =%s 符号反转后：%s'%(y,context.copy_negate(y)))# 结果为2
print('z =%s 符号反转后：%s'%(z,context.copy_negate(z)))# 结果为-0
print('m =%s 符号反转后：%s'%(m,context.copy_negate(m)))# 结果为-Infinity
print('n =%s 符号反转后：%s'%(n,context.copy_negate(n)))# 结果为Infinity
