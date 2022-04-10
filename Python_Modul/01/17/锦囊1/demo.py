import string
formatter = string.Formatter()
data = {'ID':'00001','name':'吉林省明日科技有限公司'}
fieldname = 'ID'
tuple1=formatter.get_field(fieldname,(),data)
print(tuple1)
