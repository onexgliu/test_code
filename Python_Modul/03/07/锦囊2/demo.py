from decimal import *  # 导入十进制定点和浮点运算模块

print(Decimal(12) + Decimal(100))  # 整数的加法运算
print(Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))  # 浮点数的加减混合运算
print(Decimal('0.1') * 1000)  # 浮点数的乘法运算
print(Decimal('9.5') % Decimal(2))  # 整数的求余运算
print(Decimal('9.5') / Decimal(2))  # 整数的除法运算
print(Decimal('9.5') // Decimal(2))  # 整数的整除运算
print(Decimal('9.5') * Decimal(2) / Decimal(3))  # 整数的乘除混合运算
