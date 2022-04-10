import os  # 文件与操作系统相关模块
import time # 导入时间模块
# 设置访问和修改时间
os.utime( r'e:/mr/wgh/test.txt',times = (int(time.time())-3600,int(time.time())-3600))
