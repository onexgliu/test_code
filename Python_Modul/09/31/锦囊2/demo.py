import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDONLY)  # 打开文件描述符
print(fd)  # 输出文件描述对象
print('通过fdopen()方法实现：',os.fdopen(fd))  # 返回文件描述对象所对应的文件对象
print('通过内置的open()函数实现：',open(r'test.txt','r')) # 通过open()打开文件对象
