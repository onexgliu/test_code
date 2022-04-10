import re  # 导入正则表达式re模块

pattern = re.compile('(?P<group_1>\w+) (?P<group_2>\w+)', re.I)  # 分组表达式
string = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = re.search('SHOP mr_', string)  # 匹配结果match对象
print(string)  # 打印原字符串
print(match)  # 打印需要移除的内容
print(string[:match.start()] + string[match.end():])  # 打印移除后的内容
