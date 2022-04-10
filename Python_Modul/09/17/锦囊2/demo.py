import os  # 文件与操作系统相关模块

project = input('请输入要打开的应用程序名称(如Word、MediaPlayer等)：')
if project.lower() == 'mediaplayer':
    os.startfile(r'C:\Program Files\Windows Media Player\wmplayer.exe')  # 打开Media Player
elif project.lower() == 'word':
    os.startfile(r'C:\Program Files\Microsoft Office\Office16\WINWORD.EXE')  # 打开Word
elif project.lower() == 'excel':
    os.startfile(r'C:\Program Files\Microsoft Office\Office16\EXCEL.EXE')  # 打开Excel
else:
    print('没有找到相应的程序程序！')
