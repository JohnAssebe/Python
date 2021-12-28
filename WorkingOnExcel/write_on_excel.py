#This is the program simply writes data in a Excel file 
import openpyxl
wb=openpyxl.Workbook()
newsheet=wb.create_sheet(index=1,title='newSheet')
selectsheet=wb['Sheet']
selectsheet['A1']='John Assebe'
selectsheet['A2']='Assebe skuar'
wb.save('Write.xlsx')
