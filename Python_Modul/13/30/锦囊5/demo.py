import csv


def read(file1):
    with open(file1, 'r+', newline='') as csv_file:
        reader = csv.reader(csv_file)
        return [row for row in reader]


def write(file1, rows):
    with open(file1, 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in rows:
            writer.writerow(row)


def entering_data():
    cols = int(input("请输入录入列数（整数）："))
    input_rows = []
    gogo = True
    while gogo:
        input_rows.append([input("列名 {}: ".format(i + 1)) for i in range(0, cols)])
        a = input("是否继续录入数据? (y/N): ")
        if a != "y":
            gogo = False
    write('w5.csv', input_rows)
    written_value = read('w5.csv')
    print(str(written_value))


entering_data()
