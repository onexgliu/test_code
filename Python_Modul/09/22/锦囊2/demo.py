import os  # 文件与操作系统相关模块
os.umask(0o22) # 设置权限
os.umask(0)  # 设置为默认
