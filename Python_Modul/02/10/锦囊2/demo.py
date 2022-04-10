import re
string = 'abcdefghijklmnopqrstuvwxyz我爱Python0123456789!#$%&*+-.^_`|~'# 定义需要筛选的字符串
result = re.sub("[A-Za-z0-9\u4e00-\u9fa5]", "", string)                   # 替换字符串
print(result)                                                                  # 打印替换结果
