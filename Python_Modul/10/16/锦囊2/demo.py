import os.path  # 操作路径的模块
pathlist = [r'demo\message.txt',r'E:/mr/test/pdf/list.docx',r'E:/qrcode.png']
for path in pathlist:  # 遍历目录列表
    if not os.path.isabs(path):  # 如果不是绝对路径
        path = os.path.abspath(path)  # 转换为绝对路径
    print(path)  # 输出各个路径
