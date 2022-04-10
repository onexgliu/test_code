import re  # 导入正则表达式re模块

# 获取字符串中的数字
it = re.finditer(r"\d+", "12a32bc43jf3")
# 便利获取后的迭代对象
for match in it:
    print(match.group())  # 打印数字
