﻿import os.path   # 导入os.path模块
joinpath = os.path.join(r'E:/PROGRAM/PYTHON/CODE',r'demo\hello.py')        # 拼接字符串
print('拼接后的路径：',joinpath)
print('规范后的路径：',os.path.normcase(joinpath))  # 规范路径
