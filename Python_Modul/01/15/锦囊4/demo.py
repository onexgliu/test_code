import string

formatter = string.Formatter()
s1 = '${:.2f}'  # 添加美元符号，小数保留两位
s2 = '¥{:,.2f}'  # 添加人民币符号，用千位分隔符进行区分
s3 = '£{:,.2f}'  # 添加英镑符号，用千位分隔符进行区分
s4 = '€{:.2f}'  # 添加欧元符号，保留两位小数，千位分隔
print(formatter.format(s1, 0.88))
print(formatter.format(s2, 888800))
print(formatter.format(s3, 123567))
print(formatter.format(s4, 123567))
