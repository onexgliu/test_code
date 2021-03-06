from datetime import date  # 导入datetime模块中的date类

date_object = date(2020, 7, 13)  # 创建指定日期的date对象
print(date_object.__format__('%Y-%m-%d %a %B'))  # 打印以“-”分隔的日期字符串
print(date_object.__format__('%Y/%m/%d %a %B'))  # 打印以“/”的日期字符串
print(date_object.__format__('%Y %m %d %a %B'))  # 打印以“ ”的日期字符串
