import string

formatter = string.Formatter()
list1 = ['零基础学Python', 'Python编程锦囊', 'Python从入门到项目实践']
val = formatter.format('《{}》《{}》《{}》', *list1)
print(val)
