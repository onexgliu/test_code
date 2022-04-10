from calendar import Calendar  # 导入日历模块中的Calendar类

week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', ]
calendar_obj = Calendar()  # 创建默认的Calendar对象
week_index = list(calendar_obj.iterweekdays())[0]
print('在默认情况下一周第一天为：', week_list[week_index])
