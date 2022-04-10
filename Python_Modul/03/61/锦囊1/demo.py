import decimal # 导入十进制定点和浮点运算模块
c = decimal.Context(
        prec=28, rounding=decimal.ROUND_UP,
        traps=[decimal.DivisionByZero, decimal.Overflow, decimal.InvalidOperation],
        flags=[decimal.Inexact, decimal.Rounded],
        Emax=999999,
        Emin=-999999,
        capitals=1,
        clamp=0
) # 创建decimal.Context对象
decimal.setcontext(c)  # 设置活动线程的当前上下文
print('清除标记前')
print(decimal.getcontext())  # 获取活动线程的当前上下文
decimal.getcontext().clear_flags()  # 清空flags属性
print('清除标记后')
print(decimal.getcontext())   # 获取活动线程的当前上下文
