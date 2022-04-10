import os.path   # 导入os.path模块
print(os.path.split(r'E:/mr/test/pdf/list.docx'))  # 分割绝对路径
print(os.path.split(r'E:/mr/test/pdf/'))  # 分割绝对路径
print(os.path.split(r'/test/pdf/list'))  # 分割相对路径
