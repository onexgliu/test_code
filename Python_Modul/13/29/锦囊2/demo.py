import csv
from tkinter import *

root = Tk()
root.title('读取csv文件数据')
# 单击按钮读取数据
with open('./tmp/r1.csv', 'r') as f:
    reader = csv.reader(f)


    # 定义读取下一行数据的函数rnext
    def rnext():
        print(reader.__next__())


    # 设置按钮
    b = Button(root, text='下一行', font=('KaiTi', 36, 'bold'), bg='pink', fg='green', bd=2, width=10, command=rnext)
    b.pack()
    root.mainloop()
