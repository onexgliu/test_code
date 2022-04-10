import re  # 导入正则表达式re模块
pattern = re.compile('[1-2]') # 数值替换表达式，替换字符串中的1-2
pattern2 = re.compile('g.t')  # 字幕替换表达式，替换字符串中的get、got、gut
# 需要匹配的字符串
string = '123456abcdef'
string2 = 'I get A,  I got B ,I gut C'
print(pattern.subn('A',string))               # 返回元组，包含新字符串与替换次数
print(pattern2.sub('have',string2)) # 返回新字符串
print(pattern2.subn('have',string2))# 返回元组，，包含新字符串与替换次数














