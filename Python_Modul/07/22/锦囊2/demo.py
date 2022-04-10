import datetime  # 导入datetime模块

reduce_four = datetime.timezone(datetime.timedelta(hours=-4))  # 创建-4时区对象
plus_four = datetime.timezone(datetime.timedelta(hours=4))  # 创建+4时区对象
dt = datetime.datetime.today()  # 获取当前本地日期时间对象
print(dt.astimezone())  # 打印默认时区信息的datetime对象
print(dt.astimezone(reduce_four))  # 打印修改为-4的时区
print(dt.astimezone(plus_four))  # 打印修改为+4的时区
