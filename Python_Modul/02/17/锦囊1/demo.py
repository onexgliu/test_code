import re  # 导入正则表达式re模块
pattern = re.compile('\d+')  # 正则表达式对象
string = '12a32bc43jf3' # 要匹配的字符串
it = pattern.finditer(string,2,8)
# 便利获取后的迭代对象
for match in it:
    print (match.group())  # 打印数字








