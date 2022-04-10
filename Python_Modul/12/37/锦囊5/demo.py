import sys

sys.stdout.write('请输入数字验证码：')
if sys.stdin.readline()[:-1].isdigit():
    print('正在登录程序员之家商务系统！')
else:
    print('输入了非数字字符，请重新输入！')


def inputbox(showorder, lengh):
    instr = sys.stdin.readline()[:-1]  # 读取标准输入流输入的数据，去掉最后的\n
    if len(instr) != 0:
        if showorder == 1:
            if str.isdigit(instr):
                if instr == 0:
                    print("\033[1;31;40m 输入为零，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 2:
            if str.isalpha(instr):
                if len(instr) != 3:
                    print("\033[1;31;40m必须输入三个字母，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
        if showorder == 3:
            if str.isdigit(instr):
                if len(instr) != lengh:
                    print("\033[1;31;40m必须输入" + lengh + "个数字，请重新输入！！\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40m输入非法，请重新输入！！\033[0m")
                return "0"
    else:
        print("\033[1;31;40m输入为空，请重新输入！！\033[0m")
        return "0"


import sys

sys.stdout.write('请输入5位数字验证码：')
instr = sys.stdin.readline()[:-1].strip(' ')
isgo = 'go'
if len(instr) != 5:
    print('输入非5位数字，请重新输入！')
    isgo = 'no'
else:
    for i in instr:
        if ord(i) not in range(ord('1'), ord('9')):
            print('输入了非数字字符，请重新输入！')
            isgo = 'no'
            break
if isgo == 'go':
    print('正在登录开发者之家系统！')

import sys

sys.stdout.write('注册用户名：')
instr = sys.stdin.readline()[:-1].strip(' ')
isgo = 'go'
for i in instr:
    if ord(i) in range(33, 127):
        if ord(i) in [64, 47, 92, 35]:
            print('输入了非法字符“', i, '”请重新输入！')
            isgo = 'no'
            break
    else:
        print('输入了非法字符,请重新输入！')
        isgo = 'no'
        break
if isgo == 'go':
    print('用户名注册完成，请继续填写其他注册信息！！')
