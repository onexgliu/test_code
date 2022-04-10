import os  # 文件与操作系统相关模块

info = os.stat(r'D:/Python已出版图书/cba.txt')  # 获取指定文件的信息
print('文件信息：', info)
