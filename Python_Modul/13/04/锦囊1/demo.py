import csv

with open('./tmp/a3.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_NONE)
    spamwriter.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    spamwriter.writerow(['mrkj', 4006751066, 84978981])
