import csv
import os

path = './tmp/222.csv'
with open(path, 'r', newline='') as f:
    data = csv.reader(f)
    a = next(data)
    print(a)
    i = j = 1
    for row in data:
        print(row)
        print(f'i is {i}, j is {j}')
        # 每10条数据进行分割，并生成新的文件名
        if i % 10 == 0:
            j += 1
            print(f'文件{j} 生成成功')
        path = './tmp/aa/' + str(j) + '.csv'
        # 如果文件不存在，则创建文件并写入数据
        if not os.path.exists(path):
            with open(path, 'w', newline='') as f:
                w = csv.writer(f)
                w.writerow(['n1', 'n2', 'n3', 'n4'])
                w.writerow(row)
            i += 1
        # 如果文件存在，则追加写入数据
        else:
            with open(path, 'a', newline='') as f:
                w = csv.writer(f)
                w.writerow(row)
            i += 1
