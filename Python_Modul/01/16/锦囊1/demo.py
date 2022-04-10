import string

formatter = string.Formatter()
val = '明日科技'
str1 = formatter.format_field(val, '>9')  # 右对齐
print(str1)
str1 = formatter.format_field(val, '<9')  # 左对齐
print(str1)
str1 = formatter.format_field(val, '^9')  # 中间对齐
print(str1)
