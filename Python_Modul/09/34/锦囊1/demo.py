import os  # 文件与操作系统相关模块

r, w = os.pipe()  # 创建用于读写的文件描述符(r,w)
print(os.get_handle_inheritable(w))  # 获取指定句柄的可继承标志
