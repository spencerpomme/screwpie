# Test file on transfer csv file data to sql database
import csv
import psycopg2

secret = input("Please input db password!\n")
conn = psycopg2.connect(database="douban", user="zhangpingcheng", password=secret)
curr = conn.cursor()

with open('test.csv', encoding='utf8') as csvfile:
    i = 0
    reader = csv.reader(csvfile)
    for row in reader:
        if i < 10:
            print(row)
            print(len(row))
            curr.execute("INSERT INTO gzzf VALUES (%d, '%s', '%s', '%s', '%s', %d, '%s');" % (
                 i, row[0], row[1], row[2], row[3], int(row[4]), row[5]))
            i += 1
        else:
            break
curr.close()
conn.close()
