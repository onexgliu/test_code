import string
formatter = string.Formatter()
data = ('mrsoft','001')
strtmp = '公司简称:{}{:>4s}'
strtmp = formatter.vformat(strtmp,data,{}) #将元组转换为指定格式的字符串
print(strtmp)
