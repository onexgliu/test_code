﻿import sys

sys.displayhook(2)  # 传入整数值
sys.displayhook('Test')  # 传入字符串
sys.displayhook(True)  # 传入bool值
sys.displayhook(['python', 'c'])  # 传入列表
sys.displayhook(('python', 'c'))  # 传入元组
