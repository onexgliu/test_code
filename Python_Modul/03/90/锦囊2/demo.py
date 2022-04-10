import decimal  # 导入十进制定点和浮点运算模块

context = decimal.getcontext()  # 获取上下文对象
x = decimal.Decimal(input('输入第一个数x：'))
y = decimal.Decimal(input('输入第二个数y：'))
if context.is_signed(x - y):  # 判断结果是否为负数，为真表示是负数
    print('x=%s  y=%s  x小于y！' % (x, y))
else:
    print('x=%s  y=%s  x不小于y！' % (x, y))
