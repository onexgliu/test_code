import string
import random
#十六进制颜色字符
s=string.hexdigits[0:10]+string.hexdigits[16:25]
#随机生成十六进制颜色代码
def randomcolor():
    colorArr = [c for c in s]
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color
for i in range(10):
  print(randomcolor())
