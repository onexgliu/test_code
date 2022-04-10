import time  # 导入时间模块
import os.path  # 导入os.path模块

ctime = os.path.getctime(r'E:/mr/test')  # 获取路径的创建时间
print(ctime)  # 输出秒数
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ctime)))  # 转换为日期时间
