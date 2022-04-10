import math  # 导入数学模块

gamma_value = math.gamma(0.1)  # 获取在伽马函数对应的值
fabs_value = math.fabs(gamma_value)  # 获取gamma_value的绝对值
log_value = math.log(fabs_value)  # 获取fabs_value的自然对数
print(log_value)  # 打印执行顺序结果
print(math.lgamma(0.1))  # 使用lgamma方法打印的结果
