import string
s = string.Template('本书作者 $name, 创作时间 $time') # 使用Template类构造函数
kewds = {'name':'吉林省明日科技有限公司', 'time':'2019.8'}
kewds1 = {'name':'time'}
str1 = s.safe_substitute(kewds)
print(str1) 
str1 = s.safe_substitute(kewds1)    
print(str1)  

