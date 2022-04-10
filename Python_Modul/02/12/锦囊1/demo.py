import re  # 导入正则表达式re模块
pattern_I = re.compile('\w+',flags=re.I) # 匹配模式，忽略大小写
pattern_M= re.compile('\w+',flags=re.M) # 匹配模式，多行
pattern_S = re.compile('\w+',flags=re.S) # 匹配模式，使用（.）字符匹配所有字符，包括换行符
pattern_X = re.compile('\w+',flags=re.X) # 匹配模式，忽略模式字符串中未转义的空格和注释
print('匹配模式I的标记为：',pattern_I.flags)
print('匹配模式M的标记为：',pattern_M.flags)
print('匹配模式S的标记为：',pattern_S.flags)
print('匹配模式X的标记为：',pattern_X.flags)



