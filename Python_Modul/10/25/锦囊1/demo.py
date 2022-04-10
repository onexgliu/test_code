import os.path  # 导入os.path模块

print(os.path.relpath(r'C:/Users/Administrator/dist'))  # 计算相对路径
print(os.path.relpath(r'C:/Users/Administrator/dist', 'Administrator'))  # 计算相对路径
