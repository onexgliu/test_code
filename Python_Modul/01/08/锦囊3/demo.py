import string
temp1='【学】【编程】【*】【*】，有需要请加 Q Q :400-675-1066.谢谢！'
str1 = string.punctuation + '》【】' # 引入英文符号常量，并附加自定义字符
print(temp1.translate(str.maketrans('', '', str1)))
