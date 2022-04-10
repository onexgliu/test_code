import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
os.close(fd)  # 关闭文件描述符
