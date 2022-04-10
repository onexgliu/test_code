import re  # 导入正则表达式re模块

pattern = re.compile('[0-9]+')  # 定义匹配数字的表达式
string = '12312abc1234546lskdj'  # 需要匹配的字符串
print(pattern.search(string, 0, 10))  # 打印匹配结果，匹配范围0，10
