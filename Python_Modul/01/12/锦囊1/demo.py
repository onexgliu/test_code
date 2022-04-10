import string
formatter = string.Formatter()
s1='***{:8d}***'    #指定格式右对齐
s2='***{:>15s}***'  #指定格式右对齐
print(formatter.format(s1,1000))
print(formatter.format(s2,'吉林省明日科技有限公司'))
