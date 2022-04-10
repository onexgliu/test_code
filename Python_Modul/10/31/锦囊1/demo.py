import os.path   # 导入os.path模块
print(os.path.splitext(r'E:/mr/test/pdf/list.docx'))  # 分割绝对路径
print(os.path.splitext(r'E:/mr/test/pdf/'))  # 分割没有文件名的绝对路径
print(os.path.splitext(r'mr/mot_cn.txt'))  # 分割相对路径
