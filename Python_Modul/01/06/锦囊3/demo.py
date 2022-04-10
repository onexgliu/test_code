import string
#自定义函数判断十六进制数字字符串
def ishex(s):
   for c in s:
      if c not in string.hexdigits:
          return False
   return True
while 1:
    myval=input('请输入：')
    print(ishex(myval))
