# Test file on transfer csv file data to sql database
import csv
import psycopg2
import datetime
import re

class FailDateRetrive(Exception):
    def __repr__(self):
        return "The date field retrived has error in it."


def getdate(rawstr:str)->str:
    """
    This function returns the date in 20xx-xx-xx format.
    """
    datelist = rawstr.split(" ")
    if len(datelist) == 1:
        return datelist[0]
    elif len(datelist) == 2:
        return '2016-' + datelist[0]
    else:
        raise FailDateRetrive

def main():
    """
    Main process, insert csv file into chosen database.
    """
    dtbase, usrname, secret = ('douban', 'postgres', '123456')
    """
    dtbase = input("Please input db name:\n")
    usrname = input("Please input username:\n")
    secret = input("Please input db password!\n")
    """
    conn = psycopg2.connect(database=dtbase, user=usrname, password=secret)
    curr = conn.cursor()
    with open('test.csv', encoding='utf8') as csvfile:
        i = 0
        reader = csv.reader(csvfile)
        for row in reader:
            #print(row)
            title, title_url, author, author_url, follow = row[0:5]
            datestring = getdate(row[5])
            print(title, follow, datestring)
            curr.execute("INSERT INTO kaopulove VALUES \
                         (%d,'%s','%s','%s','%s',%d,'%s')"%(i, title, title_url,
                          author, author_url, int(follow), datestring)
                         )
            i += 1
        print('done')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
