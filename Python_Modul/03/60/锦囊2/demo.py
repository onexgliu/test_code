import decimal # 导入十进制定点和浮点运算模块
context = decimal.Context(
        prec=28, rounding=decimal.ROUND_UP,
        traps=[decimal.DivisionByZero, decimal.Overflow, decimal.InvalidOperation],
        flags=[],
        Emax=999999,
        Emin=-999999,
        capitals=1,
        clamp=0
) # 创建decimal.Context对象
print('精度为：',context.prec)
print('可能出现的陷阱：',[k for k,v in context.traps.items() if v])
print('标记：',[k for k,v in context.flags.items() if v])
print('e的最大小数位数：',context.Emax)
print('e的最小小数位数：',context.Emin)
print('是否大写：',context.capitals)
print('区间限定：',context.clamp)
print('舍入模式：',context.rounding)
