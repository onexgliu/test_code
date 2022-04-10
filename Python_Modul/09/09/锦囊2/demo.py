import os  # 文件与操作系统相关模块
path = r'C:/cba.txt'  # 文件路径
spath = os.fspath(path)  # 获得路径的文件系统表示形式
try:
    if isinstance(spath, bytes):
        print(spath.replace(b'/', b'\\').lower())  # 斜杠变为反斜杠，并且转换为全小写字母
    else:
        print(spath.replace('/', '\\').lower())  # 斜杠变为反斜杠，并且转换为全小写字母
except (TypeError, AttributeError):
    print('文件路径必须是字符串或者字节类型！')
