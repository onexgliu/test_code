import os  # 文件与操作系统相关模块

print('更改前的当前工作目录：', os.getcwd())
os.chdir(r'E:/')  # 将当前工作目录更改到E盘根目录
print('更改后的当前工作目录：', os.getcwd())
