import os  # 文件与操作系统相关模块
fd = os.open(r'mot_cn_gbk.txt', os.O_RDWR)  # 打开文件描述符
context = os.read(fd,10)  # 读取指定内容
print(context)                  # 输出读取到的字符
print(context.decode('GBK'))  # 转换为GBK编码输出
os.close(fd)    # 关闭文件描述符
