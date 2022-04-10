import os.path  # 导入os.path模块

path = r'E:/mr/test/'  # 目录
if os.path.exists(path):  # 判断目录是否存在
    print(path, '目录存在！')
else:
    print(path, '目录不存在！')
