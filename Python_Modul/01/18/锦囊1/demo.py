import string

formatter = string.Formatter()
data = {'ID': '00001', 'name': '吉林省明日科技有限公司'}
key = 'ID'
mystr = formatter.get_value(key, (), data)
print(mystr)
