import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 上下文对象
x = decimal.Decimal(1000000) # 整数
y = decimal.Decimal('0.00001')  # 通过字符串创建Decimal对象，值为0.00001
print('%s 的位数为：%s'%(x,context.log10(x)+1))# 求整数位数
print('%s 的小数位数为：%s'%(y,context.abs(context.log10(y))))# 求小数位数
