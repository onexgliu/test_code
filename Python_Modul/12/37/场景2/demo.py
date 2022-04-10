import sys
sys.stdout.write('请输入三角形的三条边长:')
a,b,c=map(int,sys.stdin.readline()[:-1].split())
if a+b>c and a+c>b and b+c>a:
    print("可以构成三角形")
    if a==b and b==c and a==c:
        print("是等边三角形")
    else:
        if a==b or b==c or a==c:
            if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
                print("是等腰直角三角形")
            else:
                print("是等腰三角形")
        elif a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
                print("是直角三角形")
        else:
            print("是其他不规则形状三角形")
else:
    print("不能构成三角形")
