﻿import sys
class Test: # 定义一个类
    pass
t = Test() # 创建类的对象
print(sys.getrefcount(Test())) # Test()作为参数
print(sys.getrefcount(t)) # 对象t作为参数
