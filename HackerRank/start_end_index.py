import re
string=input()
pattern=input()
index=0
if(re.search(pattern,string[index:])):
    while re.search(pattern,string[index:]):
        start=re.search(pattern,string[index:]).start()+index
        index+=re.search(pattern,string[index:]).end()-1
        print((start,index))
else:
    print((-1,-1))
    
