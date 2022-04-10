import decimal  # 导入十进制定点和浮点运算模块

score = ['9.50', '9.10', '8.26', '7.98', '8.95', '10', '7.21']  # 要计算的一组数的列表
dscore = []  # 保存十进制数的数
for i in score:
    dscore.append(decimal.Decimal(i))  # 转换为十进制数
context = decimal.getcontext()  # 获取上下文对象
temp_max = dscore[0]  # 保存最大值的变量
for i in range(1, len(dscore)):
    temp_max = context.max(temp_max, dscore[i])  # 计算最大值
print('最大值为：', temp_max)
