# Test file on transfer csv file data to sql database
import csv
import psycopg2
import datetime
import re

'''
dtbase = input("Please input db name:\n")
usrname = input("Please input username:\n")
secret = input("Please input db password!\n")

conn = psycopg2.connect(database=dtbase, user=usrname, password=secret)
curr = conn.cursor()
'''
def getdate(rawstr:str)->str:
    """
    This function returns the date in 20xx-xx-xx format.
    """

patt = re.compile("20\d\d-[0-1]\d-[0-3]\d")
with open('test.csv', encoding='utf8') as csvfile:
    i = 0
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        title, title_url, author, author_url, follow = row[0:5]
        datestring = getdate(row[5])
        # curr.execute("INSERT INTO gzzf VALUES (%d, %d)" % (i, int(row[4])))
        i += 1
    print('done')
'''
conn.commit()
conn.close()
'''

