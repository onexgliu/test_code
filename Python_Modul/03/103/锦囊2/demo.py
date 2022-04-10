import decimal # 导入十进制定点和浮点运算模块
score = ['9.50','9.10','8.26','7.98','8.95','10','7.21'] # 要计算的一组数的列表
dscore = []  # 保存十进制数的数
for i in score:
    dscore.append(decimal.Decimal(i))  # 转换为十进制数
context = decimal.getcontext() # 获取上下文对象
temp_min = dscore[0]   # 保存最小值的变量
for i in range(1,len(dscore)):
    temp_min = context.min(temp_min,dscore[i]) # 计算最小值
print('最小值为：',temp_min)
