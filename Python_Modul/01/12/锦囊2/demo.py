import string

formatter = string.Formatter()
list1 = [400, 675, 1066]
val = formatter.format('{}-{}-{}', *list1)
print(val)
