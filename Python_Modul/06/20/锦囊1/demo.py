﻿from calendar import Calendar  # 导入日历模块中的Calendar类

calendar_obj = Calendar()  # 创建默认的Calendar对象
itermonth = calendar_obj.itermonthdates(2020, 7)  # 获取2020年7月份的日期迭代器
for i in itermonth:  # 循环遍历迭代器中的日期
    print(i)  # 打印迭代器中的日期
