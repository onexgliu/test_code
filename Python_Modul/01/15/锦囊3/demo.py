import string

formatter = string.Formatter()
s1 = '{:%}'  # 将小数格式化成百分比
s2 = '{:.0%}'  # 格式化后保留整数百分比
s3 = '{:.2%}'  # 格式化后保留两位小数的百分比
s4 = '{:10.3%}'  # 格式化后保留3位小数的10位百分比
print(formatter.format(s1, 0.1314))
print(formatter.format(s2, 0.1314))
print(formatter.format(s3, 0.1314))
print(formatter.format(s4, 0.1314))
