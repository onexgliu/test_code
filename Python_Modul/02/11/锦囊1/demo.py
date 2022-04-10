import re  # 导入正则表达式re模块
print(re.subn('[1-2]','A','123456abcdef'))                   # 返回元组，包含新字符串与替换次数
print(re.sub('g.t','have','I get A,  I got B ,I gut C'))    # 返回新字符串
print(re.subn('g.t','have','I get A,  I got B ,I gut C'))   # 返回元组，，包含新字符串与替换次数


