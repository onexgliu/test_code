import decimal # 导入十进制定点和浮点运算模块
print('原：\n',decimal.getcontext())  # 输出活动线程的当前上下文
context1 = decimal.getcontext().copy()  # 复制上下文对象
context1.clear_traps() # 清空副本的traps属性
print('副本：\n',context1)  # 输出副本
print('原：\n',decimal.getcontext())  # 输出活动线程的当前上下文
