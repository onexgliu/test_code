import os.path  # 操作路径的模块
# 获取当前Python文件的实际路径
print(os.path.realpath(os.path.basename(__file__)))
