import re  # 导入正则表达式re模块

# 需要匹配的字符串
string = "Tina is a good girl, she is cool, clever, and so on..."
match = re.compile(r'\w*oo\w*')  # 创建正则表达式对象
print(match.findall(string))  # 打印所有包含'oo'的单词
