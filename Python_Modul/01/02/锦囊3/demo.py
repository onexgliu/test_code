import random, string
def IDstr(num1, len1=8):
    f = open('./tmp/mycode.txt', 'w')
    for i in range(num1):
        #返回大小写字母和数字的组合
        chars = string.ascii_letters + string.digits
        #choice()函数从任何序列中随机选取8位字符
        s = [random.choice(chars) for i in range(len1)]
        f.write('{0}\n'.format(''.join(s)))
    f.close()
#调用函数，生成100个激活码
IDstr(100)
