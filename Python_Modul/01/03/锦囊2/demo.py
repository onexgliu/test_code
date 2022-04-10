import string
# 定义判断小写字母的函数
def check(value):
   for letter in value:
      if letter not in string.ascii_lowercase:
         return False
   return True
myval=input("请输入小写字母：")
print(check(myval))
