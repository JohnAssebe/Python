#Author :Yohannes Assebe(John Assebe)
import openpyxl
from openpyxl.styles import Font
import subprocess
wb=openpyxl.load_workbook('produceSales.xlsx')
sheet=wb['Sheet']
sheet['C23759']='=SUM(C23750:C23758)'
wb.save('Formula.xlsx')
subprocess.Popen(['start','Formula.xlsx'],shell=True)
