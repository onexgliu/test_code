from time import time   # 单独导入time模块中的time()函数
from time import localtime,asctime  # 导入time模块中的多个函数
local_time = localtime(time())   # 获取时间秒数并将该时间转换为时间元组
asc_time = asctime(localtime(time()))  # 获取当前时间并格式化时间
print('自1970年1月1日至今以秒为单位的时间：：',time())
print ("元组形式的当前时间为 :", local_time)    # 输出元组形式的当前时间
print("格式化后的当前时间为 :", asc_time)      # 输出格式化以后的时间
