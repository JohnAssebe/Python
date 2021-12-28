import openpyxl,pprint,time
wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
county={}
start=time.time()
for rows in range(2,sheet.max_row+1):
    state=sheet['B'+str(rows)].value
    country=sheet['C'+str(rows)].value
    pop=sheet['D'+str(rows)].value
    county.setdefault(state,{})
    county[state].setdefault(country,{'tracts':0,'pops':0})
    county[state][country]['tracts']+=1
    county[state][country]['pops']+=int(pop)
file=open('county.py','w')
file.write("AllData="+pprint.pformat(county))
file.close()
end=time.time()
print(end-start,end=' ')
print("seconds")

print("Done")
