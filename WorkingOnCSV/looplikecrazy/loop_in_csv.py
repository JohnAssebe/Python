import csv
import pprint
from datetime import datetime
simple={}
best_simple={}
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')
with open('simple.csv') as file_reader:
    file_reader.readline()
    for line in file_reader:
        key,value=line.strip().split(',')
        simple[key]=value
    pprint.pprint(simple)
best_simple={convert2ampm(key):value.title() for key,value in simple.items()}
pprint.pprint(best_simple)
last_update={dest:[k for k,v in best_simple.items()if v==dest] for dest in set(best_simple.values())}
pprint.pprint(last_update)

    
