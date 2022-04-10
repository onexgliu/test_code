import re  # 导入正则表达式re模块

string1 = "mr00soft"  # 需要匹配的字符串
# 匹配包括下划线在内的任何字符,并匹配前面的子表达式一次或多次
match1 = re.fullmatch('\w+', string1)
# 单个字符匹配任意次,贪婪匹配
match2 = re.fullmatch('.*', string1)
# 匹配多个数字
match3 = re.fullmatch('\d+', string1)
print(match1)
print(match2)
print(match3)
