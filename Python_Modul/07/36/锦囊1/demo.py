from datetime import datetime  # 导入datetime模块中的datetime类

dt = datetime.strptime('14/08/20 14:45', '%d/%m/%y %H:%M')
print(dt)  # 打印日期时间对象
