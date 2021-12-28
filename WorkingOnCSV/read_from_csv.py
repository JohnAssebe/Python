import csv
file=csv.reader(open('example.csv'))
for row in file:
    print('Row #'+str(file.line_num)+ ' ' +str(row))
