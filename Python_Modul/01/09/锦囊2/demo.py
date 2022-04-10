import string
a1 = 'mingrisoft.com'
b1 = chr(7)
c1 = chr(88)
print(all(c in string.printable for c in a1))
print(all(c in string.printable for c in b1))
print(all(c in string.printable for c in c1))
