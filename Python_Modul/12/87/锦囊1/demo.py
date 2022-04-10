import sys
sys._enablelegacywindowsfsencoding() # 改变默认文件系统编码和错误模式
print('文件系统编码：',sys.getfilesystemencoding()) # 输出文件系统编码
print('文件名转换错误模式：',sys.getfilesystemencodeerrors()) # 输出文件名转换时的错误模式名称
