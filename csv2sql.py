# Test file on transfer csv file data to sql database
import csv
import psycopg2

dtbase = input("Please input db name:\n")
usrname = input("Please input username:\n")
secret = input("Please input db password!\n")

conn = psycopg2.connect(database=dtbase, user=usrname, password=secret)
curr = conn.cursor()

with open('test.csv', encoding='utf8') as csvfile:
    i = 0
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        curr.execute("INSERT INTO gzzf VALUES (%d, %d)" % (i, int(row[4])))
        i += 1
    print('done')
conn.commit()
conn.close()
