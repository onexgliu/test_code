import csv

with open('./tmp/isbn.csv', 'w', newline='') as f:  # 指定newline=''，防止写入空行
    writer = csv.writer(f)
    writer.writerow(['ISBN'])
    writer.writerow(['9787567787421' + '\t'])
    writer.writerow(['9787569208542' + '\t'])
    writer.writerow(['9787569204537' + '\t'])
