import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('10.3697') # 通过字符串创建Decimal对象，值为10.3697
y = decimal.Decimal('-2.414') # 通过字符串创建Decimal对象，值为-2.414
print('x = %s 使用abs()方法得到的结果为：%s'%(x,context.abs(x)))# 结果为10.4
print('x = %s 使用copy_abs()方法得到的结果为：%s'%(y,context.copy_abs(x)))# 结果为10.3697
print('y = %s 使用abs()方法得到的结果为：%s'%(y,context.abs(y)))# 结果为2.41
print('y = %s 使用copy_abs()方法得到的结果为：%s'%(y,context.copy_abs(y)))# 结果为2.414
