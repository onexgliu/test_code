h = 1           # 初始化井深
find = False    # 用于跳出外层循环
while True:
    for a in range(1, h + 1):
        b = h - 2 * a   # 乙家绳子长度
        c = h - 3 * b   # 丙家绳子长度
        d = h - 4 * c   # 丁家绳子长度
        e = h - 5 * d   # 戊家绳子长度
        if a == h - 6 * e:
            print('甲：{}，乙：{}，丙：{}，丁：{}，戊：{}，井深：{}'.format(a,b,c,d,e,h))
            find = True
            break       # 跳出内层循环
    if find:            # 如果find为True则跳出外层循环
        break
    h += 1        # 井深加1
