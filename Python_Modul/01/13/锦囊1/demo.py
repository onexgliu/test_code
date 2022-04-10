import string

formatter = string.Formatter()
data = ('mrsoft')
strtmp = '公司简称:{}{:>4s}'
mystr = formatter.check_unused_args(data, {}, strtmp)
print(mystr)
