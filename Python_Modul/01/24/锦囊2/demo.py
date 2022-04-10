from string import Template
class MyTemplate(Template):
    delimiter = '*'
s = MyTemplate('*a省*b市*c区')
print(s.substitute(a='吉林',b='长春',c='二道'))
