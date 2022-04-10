import calendar                              # 导入日历模块
import time                                  # 导入时间模块
import random                                # 导入随机模块
start_time=time.mktime((2000,1,1,0,0,0,0,0,0))    #生成开始时间戳，自2000年1月1日00：00：00
end_time=time.mktime((2020,1,1,0,0,0,0,0,0))      #生成结束时间戳，自2020年1月1日00：00：00
for i in range(6):
    t = random.randint(start_time,end_time)   # 从开始时间至结束时间中随机抽取时间戳
    t_tuple = time.localtime(t)               # 将随机抽取的时间戳转换为时间元组
    print(t_tuple.tm_year,'年是否为闰年：',calendar.isleap(t_tuple.tm_year))

