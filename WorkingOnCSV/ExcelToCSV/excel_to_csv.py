'''
@Author:Yohannes Assebe(John)
This program converts an Excel files into csv file
'''
import os,csv,openpyxl
for excel_file in os.listdir('.'):
    if not excel_file.endswith('.xlsx'):
        continue
    wb=openpyxl.load_workbook(excel_file)
    for sheets in wb.sheetnames:
        sheet=wb[sheets]
        csv_file=open(os.path.join('csv_files',excel_file[0:-5]+"_"+sheets+".csv"),'w',newline='')
        csv_writer=csv.writer(csv_file)
        for rows in range(1,sheet.max_row+1):
            row_value=[]
            for col in range(1,sheet.max_column+1):
                row_value.append(sheet.cell(row=rows,column=col).value)
            csv_writer.writerow(row_value)
        csv_file.close()
print('done')



    
