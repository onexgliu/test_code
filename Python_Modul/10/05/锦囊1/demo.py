import os.path  # 导入os.path模块

pathlist = [r'E:/demo/temp.txt', r'E:/demo/test/test.txt', r'E:/demo/test.txt']  # 目录列表
print(os.path.commonpath(pathlist))  # 提取最长的共有路径
