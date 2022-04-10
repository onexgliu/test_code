import string

count = 0
nPos = 0
s = '《Python 项目开发案例集锦》 一书从入门学习者的角度出发，开发了 8 个开发方向、23 个项目'
for i in s:
    nPos += 1
    # 检查空白符，输出位置和个数
    if i in string.whitespace:
        count += 1
        print('空白字符位置:', nPos - 1)
print('空白字符总数：', count, '个')
