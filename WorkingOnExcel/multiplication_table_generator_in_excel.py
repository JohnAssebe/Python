'''
@Author:Yohannes Assebe
This Program Produce a multiplication Table in Excel for number less than 702
'''
import openpyxl,subprocess
import az
wb=openpyxl.Workbook()
try:
    num=int(input("Enter a number for multiplication table: "))
    sheet=wb.active
    sheet['A1'].value='X'
    columns=az.columns
    for i in range(1,num+1):
        sheet['A'+str(i+1)].value=i
    for i in range(1,num+1):
        sheet[columns[i]+str(1)].value=i
    for i in range(1,num+1):
        for k in range(1,num+1):
            sheet[columns[i]+str(k+1)].value='=PRODUCT('+columns[i]+str(1)+","+"A"+str(k+1)+')'
    wb.save("multiplication_table.xlsx")
    print("Done See the result in multiplication_table.xlsx")
    subprocess.Popen(['start','multiplication_table.xlsx'],shell=True)
except ValueError as err:
    print("Error:Please enter a Number")
except IndexError as errr:
    print("Error:Enter a number less than 702")
    


