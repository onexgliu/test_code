import os  # 文件与操作系统相关模块
defaultdir = os.getcwd()  # 获取当前工作目录
try:
    os.chdir(r'G:/mr')   # 将当前工作目录更改到G盘的mr目录
    print('当前工作目录：',os.getcwd())
except:
    print('更改的目录不存在')
finally:
    os.chdir(defaultdir)
    print('当前工作目录：',os.getcwd())
