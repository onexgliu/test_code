import random, string
#生成5组随机数
for i in range(5):
    #sample()函数从指定的序列中随机截取8个字符
    myCode=''.join(random.sample(string.ascii_letters,8))
    print(myCode)

