import string

formatter = string.Formatter()
val = 888
str1 = formatter.convert_field(val, 's')  # 转换为字符串
print(str1)
print(type(str1))
