import decimal  # 导入十进制定点和浮点运算模块

decimal.getcontext().prec = 3  # 设置精度为3
# 通过字符串类型的科学记数法指定的整数
x = decimal.Decimal('7E+7')
result = decimal.getcontext().to_eng_string(x)
print('x = %s to_eng_string(x)结果为：%s' % (x, result))
# 通过字符串类型的科学记数法指定的小数
y = decimal.Decimal('7E-7')
result2 = decimal.getcontext().to_eng_string(y)
print('y = %s to_eng_string(y)结果为：%s' % (y, result2))
# 正无穷
k = decimal.Decimal('infinity')
result3 = decimal.getcontext().to_eng_string(k)
print('k = %s to_eng_string(k)结果为：%s' % (k, result3))
# 通过字符串参数指定的小数
z = decimal.Decimal('0.1')
result4 = decimal.getcontext().to_eng_string(z)
print('z = %s to_eng_string(z)结果为：%s' % (z, result4))
# 通过数值参数指定的小数
m = decimal.Decimal(0.1)
result5 = decimal.getcontext().to_eng_string(m)
print('m = %s to_eng_string(m)结果为：%s' % (m, result5))
# 通过数值类型的科学记数法指定的整数
n = decimal.Decimal(5E+3)
result6 = decimal.getcontext().to_eng_string(n)
print('n = %s to_eng_string(n)结果为：%s' % (n, result6))
