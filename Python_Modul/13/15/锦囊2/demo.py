import csv
with open('./tmp/b1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ',quotechar='"',
                            doublequote=False,quoting=csv.QUOTE_ALL,escapechar='%')
    writer.writerow(['mrk"j'] * 5 + ['www.mingrisoft.com'])
    writer.writerow(['mrkj', 4006751066, 84978981])
