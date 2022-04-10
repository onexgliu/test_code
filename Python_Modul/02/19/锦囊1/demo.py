import re  # 导入正则表达式re模块

pattern = re.compile('[a-z]+')  # 定义匹配字母的表达式
string = '12312abc1234546lskdj'  # 需要匹配的字符串
print(pattern.match(string, 5, 10))  # 打印匹配结果，匹配范围5，10
