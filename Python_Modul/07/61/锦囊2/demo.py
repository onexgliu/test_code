import datetime  # 导入datetime模块

# 创建名称为欧洲 马德里时区
timezone_madrid = datetime.timezone(datetime.timedelta(hours=2), name='Europe/Madrid')
t_madrid = datetime.time(4, 5, 12, tzinfo=timezone_madrid)  # 为time对象设置自定义的马德里时区
# 为time对象设置自定义的马德里时区所对应的utc
t_utc = datetime.time(4, 5, 12, tzinfo=timezone_madrid.utc)
print(t_madrid)  # 打印马德里时区的time对象
print(t_utc)  # 打印马德里时区对应的utc的time对象
