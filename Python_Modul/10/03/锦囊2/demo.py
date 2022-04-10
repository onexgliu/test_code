import os.path  # 操作路径的模块

# 获取当前Python文件的绝对路径
print(os.path.abspath(os.path.basename(__file__)))
