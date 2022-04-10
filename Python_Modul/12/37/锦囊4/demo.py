import sys
sys.stdout.write('age：') # 提示用户输入
age = int(sys.stdin.readline())




import sys
sys.stdout.write('请输入您的密码：')
password = sys.stdin.readline().upper()
sys.stdout.write('请输入您的姓名：')
name = sys.stdin.readline().capitalize()
sys.stdout.write('请输入您的学校：')
school = sys.stdin.readline().title()
print(password,name,school)
