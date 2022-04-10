from datetime import datetime  # 导入datetime模块中的datetime类
dt=datetime.today()         #把获取的当前本地日期时间赋给变量dt
print('最大值：',dt.max)
print('最小值：',dt.min)
print('最小单位：',dt.resolution)
