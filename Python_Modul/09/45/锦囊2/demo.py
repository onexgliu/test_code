import os  # 文件与操作系统相关模块

fd = os.open(r'test2.txt', os.O_RDWR)
os.write(fd, '命运给予我们的不是失望之酒，而是机会之杯。'.encode('gbk'))
os.lseek(fd, 0, 0)  # 定义到文件开始
print('未解码：\n', os.read(fd, 100))
os.lseek(fd, 0, 0)  # 定义到文件开始
print('文件内容：', os.read(fd, 100).decode('gbk'))  # 读取fd中的文件内容
os.close(fd)  # 关闭文件描述符
