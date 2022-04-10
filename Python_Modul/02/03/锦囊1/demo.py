import re  # 导入正则表达式re模块
# 需要转义的字符串
string = 'abcdefghijklmnopqrstuvwxyz0123456789!#$%&*+-.^_`|~'
print(re.escape(string))  # 打印转义后的字符串

