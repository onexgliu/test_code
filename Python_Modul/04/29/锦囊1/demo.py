import math          # 导入数学模块
import decimal       # 导入十进制定点和浮点运算模块
print(math.gamma(0.1))                    # 获取浮点数值对应的伽马函数值
print(math.gamma(decimal.Decimal('0.1'))) # 获取Decimal浮点值对应的伽马函数值
print(math.gamma(1))                      # 获取整数1对应的伽马函数值
print(math.gamma(math.pi))                # 获取圆周率对应的伽马函数值
