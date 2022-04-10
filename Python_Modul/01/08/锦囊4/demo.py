import string
import collections     #集合模块
with open('./tmp/love and loss.txt') as f:#打开文本文件
    s=f.read()
for i in s:
  if i in string.punctuation:  #如果字符是标点符号就将其替换为空格
    s = s.replace(i,' ')
print(s.split())#按空格分割
str1=s.split()
#Counter统计相关元素出现的次数
print('\n各单词出现的次数：\n %s' % collections.Counter(str1))
