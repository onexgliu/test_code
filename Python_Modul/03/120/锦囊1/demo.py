import decimal # 导入十进制定点和浮点运算模块
decimal.getcontext().prec = 4  # 设置精度为4
x = decimal.Decimal('3.14159') # 一个数
y = decimal.Decimal('2') # 正数
z = decimal.Decimal('-2') # 负数
k = decimal.Decimal('0') # 零
result = decimal.getcontext().scaleb(x,y)
result2 = decimal.getcontext().scaleb(x,z)
result3 = decimal.getcontext().scaleb(x,k)
print('x = %s y = %s scaleb(x,y)结果为：%s'% (x ,y,result))
print('x = %s z = %s scaleb(x,z)结果为：%s'% (x ,z,result2))
print('x = %s k = %s scaleb(x,k)结果为：%s'% (x ,k ,result3))
