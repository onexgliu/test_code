import string

formatter = string.Formatter()
s1 = '{:0>3}'
s2 = '{:0>5}'
s3 = 'a{:0>6}'
print(formatter.format(s1, 1))
print(formatter.format(s2, '08'))
print(formatter.format(s3, 886))
