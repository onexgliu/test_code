import os  # 文件与操作系统相关模块

src = r'e:/mot.txt'  # 源路径
dst = r'e:/mr/mot.txt'  # 目标路径
os.link(src, dst)  # 创建硬链接
