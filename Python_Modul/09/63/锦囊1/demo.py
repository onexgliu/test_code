import os  # 文件与操作系统相关模块

os.symlink(r'e:/mr/mot.txt', r'e:/learn/mot.txt')  # 创建符号链接（软链接）
print(os.readlink(r'e:/learn/mot.txt'))  # 获取符号链接的指向路径
