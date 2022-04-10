import string
mychar = "\n\r| " #换行符、空格
#自定义判断可打印字符的函数
def isprint(c):
    if ord(c) > 127:
        return False
    if ord(c) < 32:
        return False
    if c in mychar:
        return False
    if c in string.printable:
        return True
    return False
while 1:
  myval=input('请输入字符：')
  print(isprint(myval))
