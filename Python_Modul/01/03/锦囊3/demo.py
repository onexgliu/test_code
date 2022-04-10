import random, string
#生成由小写字母和数字随机组成的10位密码
passwords = ''.join([random.choice(string.ascii_lowercase + string.digits)for n in range(10)])
print(passwords)
