#Author :Yohannes Assebe(John Assebe)
import openpyxl
from openpyxl.styles import Font
import subprocess
#data_only=True used to avoid getting of any formula value instead of calculated value
wb=openpyxl.load_workbook('produceSales.xlsx',data_only=True)
sheet=wb['Sheet']
fontobj1=Font(name='Calibri',size=15,bold=True)
fontobj=Font(name='Times New Roman',size=13,italic=True,bold=True)
sheet['A1'].font=fontobj1
sheet['B1'].font=fontobj1
sheet['C1'].font=fontobj1
sheet['D1'].font=fontobj1
sheet['D23759'].value=0.0
for row in range(2,sheet.max_row):
    cost=sheet['B'+str(row)].value
    if cost>=5.0:
        #finally add the total cost only that cost per pound greater than 5
        sheet['D23759'].value+=sheet['D'+str(row)].value
        sheet['D'+str(row)].font=fontobj
        sheet['C'+str(row)].font=fontobj
        sheet['B'+str(row)].font=fontobj
        sheet['A'+str(row)].font=fontobj

wb.save('Styled.xlsx')
print("Styled succesfully that have greater than $5")
subprocess.Popen(['start','Styled.xlsx'],shell=True)

