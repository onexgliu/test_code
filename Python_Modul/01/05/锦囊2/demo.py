import random, string

# 生成1组随机数
for i in range(1):
    # sample()函数从指定的序列中随机截取8个字符
    myCode = ''.join(random.sample(string.digits, 8))
    print(myCode)
