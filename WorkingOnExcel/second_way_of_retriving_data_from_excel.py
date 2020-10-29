#author:Yohannes Assebe(John Assebe)
import openpyxl
wb=openpyxl.load_workbook('defense_schedule.xlsx')
sheet=wb['Sheet1']
# We can use slice to show data partially 
for a in sheet['A1':'C11']:
    for b in a:
        if b.value==None:
            b.value=" "
        print(b.value,end="\t | \t")
        
    print()
