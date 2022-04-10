import re  # 导入正则表达式re模块

pattern = re.compile('1[34578]\d{9}')  # 定义要替换的模式字符串
string = '中奖号码为：84978981 联系电话为：13611111111'
result = pattern.sub('1XXXXXXXXXX', string)  # 替换字符串
print(result)
