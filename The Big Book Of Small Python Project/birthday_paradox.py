import datetime
import random
#help(datetime)
def generate_random_birthdates(num):
    '''Generate a random birthdays of specified numbers'''
    birthday_lst=[]
    for i in range(num):
        start_date=datetime.date(2020,1,1)
        time_delta=datetime.timedelta(random.randint(0,364))
        birth_date=start_date+time_delta
        birthday_lst.append(birth_date)
    return birthday_lst
def get_match(lst):
    '''Return Number Of Matched BD and Matched Birthdays'''
    matched_counter=0
    matched=[]
    if(len(lst)==len(set(lst))):
        return (0,[])
    for a,birth_day1 in enumerate(lst):
        for b,birth_day2 in enumerate(lst[a+1:]):
            if birth_day1==birth_day2:
                matched_counter+=2
                matched.append(birth_day1)
    return (matched_counter,matched)
                
                
months=["Jan.","Feb.","Mar.","Apr.","May.","Jun.","Jul.","Aug.","Sep.","Oct.","Nov.","Dec."]
print('''
     Enter A Number To Generate  BirthDates..
     
''')
no_birth=int(input())
generated_days=generate_random_birthdates(no_birth)
matched,matched_days=get_match(generated_days)
print("( ",end='')
for i,date_g in enumerate(generated_days):
    if(i!=len(generated_days)-1):
        print(str(months[date_g.month-1])+" "+str(date_g.day),end=" , ")
    else:
        print(str(months[date_g.month-1])+" "+str(date_g.day),end=" )")
print()
print(str(matched)+" Peoples Have The Same BirthDay")
if(len(matched_days)!=0):
    print("Birthdays :- ",end='')
    print("( ",end='')
    for i,date_g in enumerate(matched_days):
        if(i!=len(matched_days)-1):
            print(str(months[date_g.month-1])+" "+str(date_g.day),end=" , ")
        else:
            print(str(months[date_g.month-1])+" "+str(date_g.day),end=" )")

