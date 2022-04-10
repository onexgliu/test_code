from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.today()  # 把获取的当前本地日期时间赋给变量dt
print(dt)  # 打印当前本地日期时间
print(dt.year, '年')
print(dt.month, '月')
print(dt.day, '日')
print(dt.hour, '时')
print(dt.minute, '分')
print(dt.second, '秒')
print(dt.microsecond, '微秒')
print(dt.tzinfo, '时区')
