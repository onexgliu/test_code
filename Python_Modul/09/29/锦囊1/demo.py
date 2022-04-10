import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
fd2 = os.dup(fd)  # 生成副本
print('原fd对象：',fd)
print('生成的副本：',fd2)
