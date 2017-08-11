import csv
with open('csvFile.csv', 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    writer.writerow(['Mohamed', 'Full stack developer'])
    writer.writerow(['Alansary', 'Software Engineer'])
    writer.writerow(['Ansberg', 'Data Scientist'])

