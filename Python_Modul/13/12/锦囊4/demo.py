import csv

with open('./tmp/mrbook1.csv') as csvFile:
    rows = csv.reader(csvFile)
    h1 = next(rows)
    with open('./tmp/mrbook2.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in rows:
            row.append(float(row[3]) * int(row[4]))  # 追加一列“金额”
            writer.writerow(row)  # 在每行的最后一列写入“金额”
