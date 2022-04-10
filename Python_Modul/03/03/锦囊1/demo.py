import decimal # 导入十进制定点和浮点运算模块
print('靠近零：',decimal.Decimal('3.14').to_integral_value(decimal.ROUND_HALF_DOWN)) # 靠近零
print('远离零：',decimal.Decimal('3.14').to_integral_value(decimal.ROUND_UP))         # 远离零
