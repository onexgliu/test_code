import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDWR)  # 打开文件描述符
os.write(fd,'愿你的青春不负梦想！'.encode())  # 向文件中写入文字，将替换原文件的内容
os.fsync(fd)    # 强制写入到文件
os.close(fd)    # 关闭文件描述符
