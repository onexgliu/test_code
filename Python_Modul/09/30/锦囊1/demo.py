import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
print('fd：',os.fstat(fd))  # 输出fd的状态
fd2 = os.open(r'temp.py',os.O_CREAT)  # 打开文件描述符
print('fd2：',os.fstat(fd2)) # 输出fd2的状态
print(os.dup2(fd,fd2) ) # 复制文件描述符
print('fd2：',os.fstat(fd2)) # 输出复制后的fd2的状态
