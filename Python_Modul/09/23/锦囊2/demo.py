import os  # 文件与操作系统相关模块

path = r'test.txt'  # 文件路径
if os.access(path, os.F_OK):
    fd = os.open(path, os.O_RDWR)  # 打开文件描述符
    context = os.read(fd, 100)  # 读取指定内容
else:
    fd = os.open(path, os.O_CREAT | os.O_RDWR)  # 打开文件描述符
    os.write(fd, '生命美妙之处， 就在于你的勇气会成就更美的你。'.encode('gbk'))
    os.lseek(fd, 0, 0)  # 定义到文件开始
    context = os.read(fd, 100)  # 读取指定内容
print(context.decode('gbk'))  # 输出
os.close(fd)  # 关闭文件描述符
