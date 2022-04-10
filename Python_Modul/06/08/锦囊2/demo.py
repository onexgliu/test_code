import calendar                              #导入日历模块
year = int(input("请输入你要查询的年份:"))  #要查询的年份
# 使用isleap()方法判断输入的年份是否为闰年，是闰年返回True，不是闰年返回False
test_year=calendar.isleap(year)
if test_year == True:                       #条件成立
    print("闰年")
else:                                         #条件不成立
    print("不是闰年")
