import shutil   # 导入高级文件操作模块
import os  # 文件与操作系统相关模块
src = r'H:/code'  # 源路径1
src2 = r'E:/cba.txt'  # 源路径2
dst = r'H:/code2'  # 目标路径
if os.path.isdir(src):
    print(shutil.copytree(src ,dst))  # 递归复制目录树
else:
    print(shutil.copyfile(src ,dst))  # 复制文件
if os.path.isdir(src2):
    print(shutil.copytree(src2 ,dst))  # 递归复制目录树
else:
    print(shutil.copy(src2 ,dst))  # 复制文件
