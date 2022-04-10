import os  # 文件与操作系统相关模块
r,w = os.pipe()  # 创建管道
print(r,w)   # 输出
