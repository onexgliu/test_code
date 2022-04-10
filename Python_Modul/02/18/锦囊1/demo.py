import re  # 导入正则表达式re模块

pattern = re.compile('[a-z]+')  # 定义匹配字母的表达式
string = 'abcskd123jaw123'  # 需要匹配的字符串
print(pattern.fullmatch(string, 0, 5))  # 打印匹配结果，匹配范围0，5
