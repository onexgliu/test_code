import sys

for i in range(0, 3):
    sys.stdout.write('请输入用户名：')
    user = sys.stdin.readline()[:-1]
    if user == 'joe':
        sys.stdout.write('请输入密码：')
        password = sys.stdin.readline()[:-1]
        if password == '123456':
            print('恭喜你进入账户', end='')
            break
        else:
            print('输入密码错误')
    else:
        print('用户名不正确')
if user == 'joe' and password == '123456':
    print(',请执行以下操作:')
else:
    print('你是输入次数超过3次')
