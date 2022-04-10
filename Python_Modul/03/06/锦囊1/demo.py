import decimal # 导入十进制定点和浮点运算模块
with decimal.localcontext(decimal.BasicContext) as ctx:
    print(ctx)  # 输出上下文管理器中的上下文对象
