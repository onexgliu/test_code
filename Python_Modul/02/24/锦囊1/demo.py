import re  # 导入正则表达式re模块

pattern = re.compile('mr_\w+')  # 分组表达式
string = 'MR_SHOP mr_shop'  # 要匹配的字符串
match = re.search(pattern, string)  # 匹配结果match对象
print(match)  # 打印匹配的Match对象
print(match.endpos)  # 打印匹配的结束位置
