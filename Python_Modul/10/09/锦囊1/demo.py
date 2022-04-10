import os.path                                  # 导入os.path模块
path = r'E:/mr/test/hello.py'                  # 文件
if os.path.lexists(path):                      # 判断文件是否存在
    print(path,'文件存在！')
else:
    print(path,'文件不存在！')
