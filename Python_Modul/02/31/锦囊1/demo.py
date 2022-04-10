import re  # 导入正则表达式re模块

pattern = re.compile('(?P<group_1>\w+) (?P<group_2>\w+)', re.I)  # 分组表达式
string = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = re.match(pattern, string)  # 匹配结果match对象
print(match.start(), match.end())  # 打印全部分组的匹配字符串对应的开始、结束标记
print(match.start(1), match.end(1))  # 打印编号1分组的匹配字符串对应的开始、结束标记
print(match.start(2), match.end(2))  # 打印编号2分组的匹配字符串对应的开始、结束标记
# 打印分组名的匹配字符串对应的开始、结束标记
print(match.start('group_1'), match.end('group_2'))
