from calendar import Calendar  # 导入日历模块中的Calendar类

calendar_obj = Calendar()  # 创建默认的Calendar对象
itermonth = calendar_obj.itermonthdays(2020, 5)  # 获取2020年5月份日期对应天数的迭代器
for i in itermonth:  # 循环遍历迭代器中日期对应的天数
    print(i)  # 打印迭代器中日期对应的天数
