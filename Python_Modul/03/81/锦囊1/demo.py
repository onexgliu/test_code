import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
print('Emax（e的最大小数位数）：',decimal.getcontext().Emax)  # e的最大小数位数
print('prec（精度）：',context.prec)  # 精度值
print('Etop()方法的值：',context.Etop())  # 输出当前上下文的最大指数值
context.prec = 3 # 设置精度为3
print('==========更改精度为3后=============')
print('Emax（e的最大小数位数）：',decimal.getcontext().Emax)  # e的最大小数位数
print('prec（精度）：',context.prec)  # 精度值
print('Etop()方法的值：',context.Etop())  # 输出当前上下文的最大指数值
