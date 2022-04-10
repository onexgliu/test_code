import time   # 导入时间模块
import os.path                           # 导入os.path模块
mtime = os.path.getmtime(r'E:/mr/test') # 获取路径最后一次修改时间
print(mtime) # 输出秒数
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(mtime))) # 转换为日期时间
