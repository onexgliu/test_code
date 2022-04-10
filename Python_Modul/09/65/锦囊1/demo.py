import os                           # 文件与操作系统相关模块
os.chdir(r'E:/mr')                # 切换当前工作目录
print(os.listdir(os.getcwd()))  # 显示当前工作目录下的全部文件及目录
os.unlink( r'mot_cn.txt')       # 删除文件
print(os.listdir(os.getcwd())) # 显示当前工作目录下的全部文件及目录
