#Author by Yohannes Assebe
import openpyxl,subprocess
wb=openpyxl.load_workbook('produceSales.xlsx')
sheet=wb['Sheet']
product_need_update={'Celery':1.91,'Garlic':3.07,'Lemon':1.27}
for rows in range(2,sheet.max_row+1):
    product=sheet['A'+str(rows)].value
    if product in product_need_update:
        sheet['B'+str(rows)].value=product_need_update[product]
       
wb.save('Productsaleupdate.xlsx')
#this snippet opens the Productsaleupdate.xlsx after update
subprocess.Popen(['start','Productsaleupdate.xlsx'],shell=True)
print("updated succesfully")
    
