from string import Template
import datetime
#字符串模板
s = Template('今日：$date 温度：$TEMP 空气质量：$air')
print(s.substitute(date=datetime.datetime.now(), TEMP='22',air='优'))
