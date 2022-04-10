import os  # 文件与操作系统相关模块

if os.name == 'posix':  # 如果是Unix操作系统
    tempname = '/home/python/mr'
    mode = ((os.stat(tempname).st_mode) | 0o555) & 0o7777
    os.chmod(tempname, mode)  # 设置路径模式
