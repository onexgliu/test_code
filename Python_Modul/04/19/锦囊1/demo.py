import math          # 导入数学模块
import decimal       # 导入十进制定点和浮点运算模块
print(math.erf(0))                      # 获取0的误差值
print(math.erf(0.1))                    # 获取浮点数值的误差值
print(math.erf(decimal.Decimal('0.1'))) # 获取Decimal浮点值的误差值
print(math.erf(1))                      # 获取整数1的误差值
print(math.erf(math.pi))                # 获取圆周率误差值
