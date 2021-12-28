#author:Yohannes Assebe(John)
import csv,os
#make dir that is called 'headerRemoved
os.makedirs('headerRemoved',exist_ok=True)
#loop over a filename in current working directories
for filename in os.listdir('.'):
    csv_rows=[]
    #skip if a file is not endwith .csv
    if not filename.endswith('.csv'):
        continue
    csvfileobj=open(filename)
    reader_obj=csv.reader(csvfileobj)
    for row in reader_obj:
        if reader_obj.line_num==1:
            continue
        csv_rows.append(row)
    csv_file_for_writer=open(os.path.join('headerRemoved',filename),'w',newline='')
    csv_writer_object=csv.writer(csv_file_for_writer)
    for rows in csv_rows:
           csv_writer_object.writerow(rows)
    csvfileobj.close()
    csv_file_for_writer.close()
    print("Removing header from   "+filename)


