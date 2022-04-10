import string

formatter = string.Formatter()
val = '明日科技'
str1 = formatter.format_field(val, '*^30')  # *符号充当占位符
print(str1)
str1 = formatter.format_field(val, '-^20')  # -符号充当占位符
print(str1)
