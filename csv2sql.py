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

def createTable(cursor, tbname:str):
    """
    This function create a new table in database.
    tbname: the name of to be created table
    configDict: field name as key and tuple (type, constrain) as value

    """
    cursor.execute("""
            CREATE TABLE %s (
            id INTEGER PRIMARY KEY,
            title VARCHAR(256) ,
            title_url VARCHAR(256),
            author VARCHAR(256),
            author_url VARCHAR(256),
            follow INTEGER ,
            lastres DATE NOT NULL);
            """ % tbname)
    print("Table %s created.\n" % tbname)


def csv2sql(filename:str, tablename: str, cursor):
    """
    Main process, insert csv file into chosen database.

    dtbase = input("Please input db name:\n")
    usrname = input("Please input username:\n")
    secret = input("Please input db password!\n")
    """
    with open(filename, encoding='utf8') as csvfile:
        i = 0
        reader = csv.reader(csvfile, cursor)
        createTable(cursor, tablename)
        for row in reader:
            #print(row)
            title, title_url, author, author_url, follow = row[0:5]
            datestring = getdate(row[5])
            print(title, follow, datestring)
            print('61: start cursor execute')
            cursor.execute("""INSERT INTO kaopulove VALUES
                           (%d,'%s','%s','%s','%s',%d,'%s');
                           """ % (i, title, title_url,
                            author, author_url, int(follow), datestring)
                           )
            print('66: end cursor execute')
            i += 1
        print('done')

if __name__ == "__main__":
    tablename = "kaopulove"
    dtbase, usrname, secret = ('douban', 'zhangpingcheng', '123456')
    conn = psycopg2.connect(database=dtbase, user=usrname, password=secret)
    curr = conn.cursor()
    # createTable(curr, tablename)
    curr.execute("drop table %s;" % tablename)
    csv2sql("kplv.csv", tablename, curr)
    conn.commit()
    conn.close()
    print("transaction finished.")
