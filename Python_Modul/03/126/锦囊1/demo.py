import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
context.prec = 3 # 设置精度为3
x = decimal.Decimal('3.1415926')
y = decimal.Decimal(1E+10)
z = decimal.Decimal(50E-14)
m = decimal.Decimal('0.000000000000001')
result = context.to_sci_string(x)
print('x = %s to_sci_string(x)结果为：%s'% (x,result))
result2 = context.to_sci_string(y)
print('y = %s to_sci_string(y)结果为：%s'% (y,result2))
result3 = context.to_sci_string(z)
print('z = %s to_sci_string(k)结果为：%s'% (z ,result3))
result4 = context.to_sci_string(m)
print('m = %s to_sci_string(m)结果为：%s'% (m ,result4))
