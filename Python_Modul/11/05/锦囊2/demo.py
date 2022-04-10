import shutil   # 导入高级文件操作模块
try:
    shutil.copyfile('E:/test2.txt','test.txt') # 目标文件为只读属性
except Exception as e:
    print('出错了！',e)
try:
    shutil.copyfile('E:/test3.txt','E:/test.txt') # 源文件不存在
except Exception as e:
    print('出错了！',e)
try:
    shutil.copyfile('E:/test2.txt','E:/test2.txt') # 源文件和目标文件相同
except Exception as e:
    print('出错了！',e)
