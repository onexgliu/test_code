import re  # 导入正则表达式re模块

pattern = re.compile('mr_\w+')  # 正则表达式对象
string = 'mr_SHOP mr_shop'  # 要匹配的字符串
match = pattern.findall(string)  # 搜索字符串
print(match)  # 输出匹配结果
print(pattern.findall(string, 0, 5))  # 打印下标0~5的结果
