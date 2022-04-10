import re  # 导入正则表达式re模块

pattern = re.compile('(?P<group_1>\w+) (?P<group_2>\w+)', re.I)  # 分组表达式
string = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = re.match(pattern, string)  # 匹配结果match对象
print(match.span(1))  # 打印分组编号1匹配字符串对应的开始、结束标记
print(match.span('group_2'))  # 打印分组名group_2匹配字符串对应的开始、结束标记
