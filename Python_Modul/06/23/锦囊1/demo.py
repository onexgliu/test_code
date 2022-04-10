﻿from calendar import Calendar  # 导入日历模块中的Calendar类

calendar_obj = Calendar()  # 创建默认的Calendar对象
itermonth = calendar_obj.itermonthdays3(2020, 8)  # 获取2020年8月份内的（年、月、日）
for i in itermonth:  # 循环遍历迭代器中的（年、月、日）
    print(i)  # 打印迭代器中（年、月、日）
