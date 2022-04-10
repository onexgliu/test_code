import string

formatter = string.Formatter()
# 类型转换
s1 = '{:d}'  # 十进制
s2 = '{:o}'  # 八进制
s3 = '{:x}'  # 十六进制
s4 = '{:f}'  # 浮点型
s5 = '{:e}'  # 浮点型(科学计数)
s6 = '{:b}'  # 布尔型
s7 = '{:s}'  # 字符串
s8 = '{:c}'  # ASCII码
print(formatter.format(s1, 1000))
print(formatter.format(s2, 1000))
print(formatter.format(s3, 1000))
print(formatter.format(s4, 1000))
print(formatter.format(s5, 1000))
print(formatter.format(s6, True))
print(formatter.format(s7, 'A'))
print(formatter.format(s8, 34))
