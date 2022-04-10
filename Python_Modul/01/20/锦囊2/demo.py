import string
formatter = string.Formatter()
data = {'ID':'00001','name':'吉林省明日科技有限公司'}
mystr = '公司名称:{ID}{name}'
mystr = formatter.vformat(mystr,(),data) # 将字典转换为指定格式的字符串
print(mystr)
