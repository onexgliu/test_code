import string
while 1:
  mystr=input('请输入有效字符：')
  if mystr in string.whitespace:
     print('输入无效，请重新输入')
  else:
     print('输入有效！')
     break
