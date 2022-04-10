import decimal # 导入十进制定点和浮点运算模块
decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('3.14159') # 5位小数
y = decimal.Decimal('3.14') # 两位小数
z = decimal.Decimal('-3.14') # 两位小数
k = decimal.Decimal('6.28') # 两位小数
result = decimal.getcontext().same_quantum(x,y)
result2 = decimal.getcontext().same_quantum(y,z)
result3 = decimal.getcontext().same_quantum(y,k)
print('x = %s y = %s same_quantum(x,y)结果为：%s'% (x ,y,result))
print('y = %s z = %s same_quantum(y,z)结果为：%s'% (y ,z,result2))
print('y = %s k = %s same_quantum(y,k)结果为：%s'% (y ,k ,result3))
