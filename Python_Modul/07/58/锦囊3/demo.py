from datetime import timedelta  # 导入datetime模块中的timedelta类
from datetime import datetime  # 导入datetime模块中的datetime类

print("现在时间:", datetime.now())
print("2天后:", datetime.now() + timedelta(2))  # 2天后
print("3天前:", datetime.now() + timedelta(-3))  # 3天前
print("1小时后:", datetime.now() + timedelta(hours=1))  # 1小时后
print("4小时前:", datetime.now() + timedelta(hours=-4))  # 4小时前
print("2小时20秒后:", datetime.now() + timedelta(hours=2, seconds=20))  # 2小时20秒后
