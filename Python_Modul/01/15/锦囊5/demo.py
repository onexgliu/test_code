import string
import datetime

formatter = string.Formatter()
d = datetime.datetime.now()  # 获取当前系统时间
s1 = '{:%Y-%m-%d %H:%M:%S}'
s2 = '{:%Y-%m-%d %H:%M:%S %a}'
s3 = f'{d:%Y}年{d:%m}月{d:%d}日 {d:%H}时{d:%M}分{d:%S}秒'
print(formatter.format(s1, d))  # 四位年
print(formatter.format(s2, d))  # 带星期的日期
print(formatter.format(s3, d))  # 中文年月日显示
