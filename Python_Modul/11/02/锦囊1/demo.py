import shutil   # 导入高级文件操作模块
import os    # 导入os模块
from pathlib import Path
import pwd
path = os.path.join(os.getcwd(),'test.txt')  # 连接路径
shutil.chown(path,user=Path(path).owner(),group=Path(path).group()) # 更改所有者用户和组
pwd.getpwuid(os.stat(path).st_uid)[0]
