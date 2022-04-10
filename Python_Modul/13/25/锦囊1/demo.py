import csv
from io import StringIO
import textwrap

# 注册新的方言
csv.register_dialect('escaped',
                     escapechar='\\',
                     doublequote=False,
                     quoting=csv.QUOTE_NONE)
csv.register_dialect('singlequote',
                     quotechar="'",
                     quoting=csv.QUOTE_ALL)
# 以不同的方言写入csv文件
data = []
for name in sorted(csv.list_dialects()):
    # 数据写入缓存
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    writer.writerow(('公司', 1, '2019-09-05', '吉林省明日科技有限公司'))
    data.append((name, dialect, buffer.getvalue()))
# 检测方言，解析数据
sniffer = csv.Sniffer()
for name, expected, sample in data:
    print('方言: "{}"'.format(name))
    print('原数据: {}'.format(sample.rstrip()))
    dialect = sniffer.sniff(sample, delimiters=',\t')
    reader = csv.reader(StringIO(sample), dialect=dialect)
    print('解析数据:\n  {}\n'.format(
        '\n  '.join(repr(r) for r in next(reader))))
