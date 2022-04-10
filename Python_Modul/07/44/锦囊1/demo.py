from datetime import datetime  # 导入datetime模块中的datetime类
import time                    # 导入时间模块
#以time.time()方法获取的时间戳为参数创建一个UTC时间的datetime对象
print(datetime.utcfromtimestamp(time.time()))
