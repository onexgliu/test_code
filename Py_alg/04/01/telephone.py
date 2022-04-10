TelephoneBook=dict(阿美='187-6667-****',阿彪='186-****-4544',爸爸='136-9475-****',白雪='136-1231-****',陈明='178-****-9490')#创建散列表
print("电话薄信息如下：")#提示
print(TelephoneBook)#输出完整散列表
print('')
print("查找联系人“白雪”的信息：")#提示
print("姓名：白雪 电话号码：",TelephoneBook['白雪'])#查找白雪信息并输出
print('')
TelephoneBook['彩虹']="188-****-5556"#添加“彩虹”信息
print("添加彩虹之后的完整电话薄：")#提示
print(TelephoneBook)#输出添加之后的完整散列表
print('')
TelephoneBook['阿彪']="178-****-5555"#修改“阿彪”信息
print("修改阿彪之后的完整电话薄：")#提示
print(TelephoneBook)#输出修改之后的完整散列表
print('')
del TelephoneBook['白雪']#删除“白雪”信息
print("删除白雪之后的完整电话薄：")#提示
print(TelephoneBook)#输出删除之后的完整散列表
