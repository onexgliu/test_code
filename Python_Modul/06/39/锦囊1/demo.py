from calendar import TextCalendar  # 导入日历模块中TextCalendar类

textcalendar_object = TextCalendar()  # 创建TextCalendar对象
print(textcalendar_object.formatyear(2020, m=6))  # 打印2020年中所有月份的字符串类型日历
