import decimal # 导入十进制定点和浮点运算模块
number = input('请输入要判断的数的字符串形式：')
context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(number) # 转换为Decimal对象
if context.is_subnormal(x):
    print('您输入的不是正规数！')
else:
    print('该数为正规数')
