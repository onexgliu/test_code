import os  # 文件与操作系统相关模块

fd = os.open(r'test.txt', os.O_RDWR)  # 打开文件描述符
print('原fd对象：', fd)
fd2 = os.dup(fd)  # 生成副本
print(os.read(fd, 100).decode('gbk'))
print('生成的副本：', fd2)
os.write(fd2, '愿你的青春不负梦想！'.encode('gbk'))  # 通过副本写入文件内容
os.lseek(fd2, 0, 0)  # 定义到文件开始
print('生成的副本：', os.read(fd2, 100).decode('gbk'))  # 读取文件内容
os.lseek(fd, 0, 0)  # 定义到文件开始
print('原fd对象：', os.read(fd, 100).decode('gbk'))
os.closerange(fd, fd2)  # 关闭原fd对象和其副本
