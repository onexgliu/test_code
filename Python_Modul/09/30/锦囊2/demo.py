import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
print('fd：',os.read(fd,100).decode('gbk'))  # 读取fd中的文件内容
fd2 = os.open(r'lift.txt',os.O_CREAT)  # 打开文件描述符
print('fd2：',os.read(fd2,100).decode('gbk'))  # 读取fd2中的文件内容
os.dup2(fd,fd2)  # 复制文件描述符
os.lseek(fd2,0,0)  # 定义到文件开始
print('重复后再次读取fd2：',os.read(fd2,100).decode('gbk'))  # 读取fd2中的文件内容
os.closerange(fd,fd2)  # 关闭原fd对象和其副本
