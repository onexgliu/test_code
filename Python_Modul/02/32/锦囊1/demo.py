import re  # 导入正则表达式re模块
pattern = re.compile('(?P<group_1>\w+) (?P<group_2>\w+)',re.I)  # 分组表达式
string = 'MR_SHOP mr_shop' # 要匹配的字符串
match=re.match(pattern,string)  # 匹配结果match对象
print(match[1])  # 打印分组1内容
print(match[2])  # 打印分组2内容
# 第一种替换方式，\1 \2 替换分组1和2的内容
print(match.expand(r'first_ \1 \2'))
# 第二种替换方式，\g<1> \g<2>替换分组1和2的内容
print(match.expand('second_ \g<1> \g<2>'))
# 第三种替换方式，\g<group_1> \g<group_2>替换分组1和2的内容
print(match.expand('third_ \g<group_1> \g<group_2>'))
