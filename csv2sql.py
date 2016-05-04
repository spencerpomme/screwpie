# Test file on transfer csv file data to sql database
import csv
with open('test.csv', encoding='utf8') as csvfile:
    i = 0
    reader = csv.reader(csvfile)
    for row in reader:
        if i < 10:
            print(row)
            print(type(row))
            i += 1
        else:
            break
