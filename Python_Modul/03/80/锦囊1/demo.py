import decimal # 导入十进制定点和浮点运算模块
context = decimal.getcontext()  # 获取上下文对象
print('Emin（e的最小小数位数）：',decimal.getcontext().Emin)  # e的最小小数位数
print('prec（精度）：',context.prec)  # 精度值
print('Etiny()方法的值：',context.Etiny())  # 输出当前上下文的最小指数值
context.prec = 3 # 设置精度为3
print('==========更改精度为3后=============')
print('Emin（e的最小小数位数）：',decimal.getcontext().Emin)  # e的最小小数位数
print('prec（精度）：',context.prec)  # 精度值
print('Etiyn()方法的值：',context.Etiny())  # 输出当前上下文的最小指数值
