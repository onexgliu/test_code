import decimal  # 导入十进制定点和浮点运算模块

x = decimal.Decimal(input('请输入第一个数：'))  # 一个数
y = decimal.Decimal(input('请输入第二个数：'))  # 第二个数
result = decimal.getcontext().compare_signal(x, y)  # 比较两个数
if result == 1:
    print('第一个数大。')
elif result == -1:
    print('第二个数大。')
elif result == 0:
    print('两个数一样大。')
