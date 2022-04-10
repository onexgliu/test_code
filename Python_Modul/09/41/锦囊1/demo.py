import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDWR)  # 打开文件描述符
os.lseek(fd,3,0)  # 设置当前位置为从文件开始的第2个字（1个汉字占3字节）
print(os.read(fd,24).decode('utf-8'))  # 读取并输出文件内容
