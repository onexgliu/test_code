import shutil   # 导入高级文件操作模块
result = shutil.disk_usage(r'E:/mr/test/pdf')  # 获取E盘的使用情况
print(result)
