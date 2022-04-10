import string
myTemplate = string.Template('本书作者:$name\n创作时间:$time') # 使用Template类创建模板
print(myTemplate.substitute(name='明日科技', time='2019年8月')) # 替换模板内容
