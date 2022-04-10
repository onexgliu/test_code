import string
formatter = string.Formatter()
strtmp = '公司简称:{}{:>4s}'
strtuple = formatter.parse(strtmp)
#遍历数据对象
for i, j in enumerate(strtuple):
    print(i, j)
