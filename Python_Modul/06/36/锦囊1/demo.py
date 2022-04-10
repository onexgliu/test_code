from calendar import HTMLCalendar      # 导入日历模块中的HTMLCalendar类
htmlcalendar_object = HTMLCalendar()    # 创建HTMLCalendar对象
html_bytes = htmlcalendar_object.formatyearpage(2020) # 获取字节类型的html页面代码
print(html_bytes.decode(encoding='utf-8')) # 打印2020年日历对应的html页面代码

