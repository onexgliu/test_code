from calendar import Calendar     # 导入日历模块中的Calendar类
calendar_obj = Calendar()          # 创建默认的Calendar对象
week_list= calendar_obj.monthdatescalendar(2020,8) # 获取2020年8月份的周列表，该列表为二维列表
for i in week_list:               # 循环遍历列表中的周列表
    print(i)                      # 打印周列表

