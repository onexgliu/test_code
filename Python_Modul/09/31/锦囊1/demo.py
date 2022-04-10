import os  # 文件与操作系统相关模块
fd = os.open(r'test.txt',os.O_RDWR)  # 打开文件描述符
print(fd)  # 输出文件描述对象
f = os.fdopen(fd,'w+')  # 返回文件描述对象所对应的文件对象
print('文件对象：',f)
print('当前输入点：',f.tell())     # 当前输入点的位置
f.write('愿你的青春不负梦想！')   # 写入内容到文件
f.flush()  # 输出缓冲区
os.lseek(fd,0,0)  # 定义到文件开始
content = os.read(fd,100)  # 读取前100个字符
print(content)
print(content.decode('gbk'))  # 转为GBK编码输出
f.close()  # 关闭文件对象
