import shutil   # 导入高级文件操作模块
# 复制目录树（忽略全部.docx文件和以l开头的全部文件）
shutil.copytree(r'E:\mr\test\pdf',r'E:\mr\test\pdf1',ignore=shutil.ignore_patterns('*.docx','l*'))
