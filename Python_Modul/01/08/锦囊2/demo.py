import string
temp = '想做/ 兼_职/程序员_/ 的 、加,我Q：  400*765@1066.！！？？有,惊,喜,哦'
print(temp.translate(str.maketrans('', '', string.punctuation)))
