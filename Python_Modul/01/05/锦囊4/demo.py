import string
#自定义函数判断手机号
def isdigits(s):
   for c in s:
      if c not in string.digits:
          return False
   if len(s)!=11:
      return False
   if s[0]=='0':
      return False
   return True
while 1:
    myval=input('请输入手机号：')
    print(isdigits(myval))
