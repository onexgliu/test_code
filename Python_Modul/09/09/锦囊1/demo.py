import os  # 文件与操作系统相关模块

path1 = r'C:/temp\cba.txt'  # 文件路径
spath1 = os.fspath(path1)  # 获得路径的文件系统表示形式
print(spath1)
path2 = b'C:/temp/cba.txt'  # 文件路径
spath2 = os.fspath(path2)  # 获得路径的文件系统表示形式
print(spath2)
path3 = ['C:/temp/cba.txt']  # 文件路径
if isinstance(path3, (str, bytes)):  # 如果输入的路径是str或者bytes对象
    spath3 = os.fspath(path3)  # 获得路径的文件系统表示形式
    print(spath3)
else:
    print('路径不是字符串或者字节对象！')
