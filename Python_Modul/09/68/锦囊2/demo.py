import os  # 文件与操作系统相关模块

fd = os.open(r'test.txt', os.O_RDWR)  # 打开文件描述符
os.write(fd, '我命由我不由天'.encode('UTF-8'))  # 向文件中写入文字，将替换原文件中部分内容
os.close(fd)  # 关闭文件描述符
