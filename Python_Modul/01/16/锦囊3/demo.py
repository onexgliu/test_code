import string
formatter = string.Formatter()
val1=5
str1=formatter.format_field(val1,'0>2')    #数字补0，填充左边，长度为2
print(str1)
str1=formatter.format_field(val1,'x<4')    #数字补x，填充右边，长度为4
print(str1)
str1=formatter.format_field(val1,'x^3')    #数字补x，填充左右，长度为3
print(str1)
