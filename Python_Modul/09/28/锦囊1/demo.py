import os  # 文件与操作系统相关模块

fd = os.open(r'test.txt', os.O_RDONLY)  # 打开文件描述符
print(os.device_encoding(fd))  # 返回设备描述字符
