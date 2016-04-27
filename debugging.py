import csv
s = '♥'

txtfile = open('debugging.txt', 'w', newline='', encoding='utf8')
csvfile = open('debugging.csv', 'w', newline='', encoding='utf8')
txtfile.write(s)
txtfile.close()
writer = csv.writer(csvfile)
writer.writerow([s])
csvfile.close()
