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
class FailDateRetrive(Exception):
    def __repr__(self):
        return "The date field retrived has error in it."


def getdate(rawstr:str)->str:
    """
    This function returns the date in 20xx-xx-xx format.
    """
    datelist = rawstr.split(" ")
    if len(datelist) == 1:
        return datelist
    elif len(datelist) == 2:
        return '2016-' + datelist[0]
    else:
        raise FailDateRetrive

def main():
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

