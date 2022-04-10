import shutil   # 导入高级文件操作模块
import os  # 文件与操作系统相关模块
paint = shutil.which('mspaint')  # 获取Windows 10系统中的画图软件的路径
os.execv(paint,['/'])  # 执行系统自带的画图程序
