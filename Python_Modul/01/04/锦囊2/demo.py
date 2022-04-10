import string
# 定义判断大写字母的函数
def check(value):
   for letter in value:
      if letter not in string.ascii_uppercase:
         return False
   return True
myval=input("请输入大写字母：")
if check(myval)==False:
   print("请输入大写字母！")
