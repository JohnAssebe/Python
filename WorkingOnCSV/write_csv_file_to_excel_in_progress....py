'''
@Author:Yohannes Assebe(John Assebe)
This program writes a Removed header of csv file to Excel file
'''
import openpyxl,csv,subprocess
wb=openpyxl.Workbook()
wb_sheet=wb['Sheet']
file=open('example.csv')
csv_reader=csv.reader(file)
rows=[]
rows_for_excel=['A','B','C','D','E','F','G']
for row in csv_reader:
    if csv_reader.line_num==1:
        continue
    rows.append(row)
print(rows)
for row in range(0,csv_reader.line_num-1):
    for each_entry in range(0,3):
##             wb_sheet[rows_for_excel[each_entry]+str(entry+1)]=rows[row][entry]
            print(rows_for_excel[each_entry]+str(each_entry+1))
wb.save('example.xlsx')
subprocess.Popen(['start','example.xlsx'],shell=True)
    
    
    
