import string
f = open('./tmp/test4.txt', 'r')
s=f.read()
for c in string.digits:
    print(c)
    s=s.replace(c,'')
print(s)
