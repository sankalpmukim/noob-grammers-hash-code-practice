import csv
with open('data.csv',newline='') as File:
    m=csv.reader(File)
    for row in m:
        print(len(row))
        break