import os  # 文件与操作系统相关模块
import stat  # 导入stat模块

os.chmod(r'cba.txt', stat.S_IWRITE)  # 将路径模式更改为写模式
