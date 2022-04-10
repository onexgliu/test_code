import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
print('通过os.open()方法打开的文件描述符：\n',os.fstat(fd))  # 输出文件描述符的状态
r,w = os.pipe()  # 创建管道
print('通过os.pipe()方法打开的文件描述符：\n',os.fstat(r))  # 输出文件描述符的状态
