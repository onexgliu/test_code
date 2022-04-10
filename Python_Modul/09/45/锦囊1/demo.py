import os  # 文件与操作系统相关模块
fd = os.open(r'test2.txt',os.O_RDWR)
print(fd)  # 输出文件描述符
os.write(fd,'Our destiny offers not the cup of despair , but the chalice of opportunity'.encode())
os.lseek(fd,0,0)  # 定义到文件开始
print('文件内容：',os.read(fd,1000).decode())  # 读取fd中的文件内容
os.close(fd)    # 关闭文件描述符
