import csv
with open('./tmp/b1.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='；',
                            quotechar='|')
    spamwriter.writerow(['mrkj'] * 5 + ['www.mingrisoft.com'])
    spamwriter.writerow(['mrkj', 4006751066, 84978981])
