import csv
with open('csvFile.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader: print(row)

