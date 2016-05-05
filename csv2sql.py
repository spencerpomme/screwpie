# Test file on transfer csv file data to sql database
import csv
import psycopg2

conn = psycopg2.connect("dbname=douban user=postgres password=123456")
curr = conn.cursor()

with open('test.csv', encoding='utf8') as csvfile:
    i = 0
    reader = csv.reader(csvfile)
    for row in reader:
        if i < 10:
            print(row[-1])
            print(type(row[-1]))
            i += 1
        else:
            break
