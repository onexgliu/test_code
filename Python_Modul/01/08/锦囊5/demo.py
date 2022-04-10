import string

s = '学编程**,有需要请加企业Q Q :400-675-1066.谢谢!'
for i in s:
    if i in string.punctuation:
        print("标点符号: " + i)
