import re  # 导入正则表达式re模块
pattern = re.compile('(?P<group_1>\w+) (?P<group_2>\w+)')  # 分组表达式
print(pattern.pattern)






