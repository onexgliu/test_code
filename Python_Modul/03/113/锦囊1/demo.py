import decimal # 导入十进制定点和浮点运算模块
decimal.getcontext().prec = 3  # 设置精度为3
x = decimal.Decimal('2') # 正数
y = decimal.Decimal('-3') # 负数
z = decimal.Decimal('0') # 零
k = decimal.Decimal('2000')  # 超过精度的数
result = decimal.getcontext().power(x,y)
result2 = decimal.getcontext().power(y,z)
result3 = decimal.getcontext().power(z,x)
result4 = decimal.getcontext().power(k,x)
print('x = %s y = %s power(x,y)结果为：%s'% (x ,y,result))
print('y = %s z = %s power(y,z)结果为：%s'% (y ,z,result2))
print('z = %s x = %s power(z,x)结果为：%s'% (z ,x ,result3))
print('k = %s x = %s power(k,x)结果为：%s'% (k ,x ,result4))
