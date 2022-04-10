from datetime import *        # 导入datetime模块中的所有函数、类以及变量
today_date = date.today()          # 获取当前日期的date对象
time_object = time(14,14,59,899)   # 创建指定时间的time对象
date_time = datetime.now()         # 获取根据当前日期与时间所创建的datetime对象
print('当前日期：',today_date)
print('指定时间为：',time_object)
print('当前日期与时间为：',date_time)
print('当前月份为：',date_time.month)
