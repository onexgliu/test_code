import math          # 导入数学模块
import decimal       # 导入十进制定点和浮点运算模块
print(math.erfc(0))                      # 获取0的互补误差值
print(math.erfc(0.1))                    # 获取浮点数值的互补误差值
print(math.erfc(decimal.Decimal('0.1'))) # 获取Decimal浮点值的互补误差值
print(math.erfc(1))                      # 获取整数1的互补误差值
print(math.erfc(math.pi))                # 获取圆周率互补误差值
