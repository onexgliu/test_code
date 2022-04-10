import shutil   # 导入高级文件操作模块
import os  # 文件与操作系统相关模块
src = r'mr'  # 被压缩文件的路径
dst = os.path.basename(src)  # 获取最后一级文件夹名，将做为压缩包的名称
print(shutil.make_archive(dst,'zip',base_dir = src)) # 压缩文件
