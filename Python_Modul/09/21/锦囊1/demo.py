import os  # 文件与操作系统相关模块

times = os.times()  # 返回当前的全局进程时间
print(times)  # 返回当前的全局进程时间
print('用户时间：', times.user)
print('系统时间：', times.system)
print('所有子进程的用户时间：', times.children_user)
