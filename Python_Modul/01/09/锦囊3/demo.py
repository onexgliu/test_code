import string
a1 = 'mingrisoft.com'
b1 = chr(7)
printset = set(string.printable)
a1set = set(a1)
b1set = set(b1)
#判断集合中的所有元素是否都包含在可打印字符集合中
print(a1set.issubset(printset))
print(b1set.issubset(printset))
