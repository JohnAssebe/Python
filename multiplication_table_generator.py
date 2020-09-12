print('''
Author:Yohannes Assebe
Multiplication Table Generator
''')
try:
    print('''
       To see the multiplication table accuratly Enter numbers less than 20
       it is possible to calculate more than 20 but it not visible accuratly
       maximum the window
     ''')
    num=int(input("Enter a number for multiplication table: "))
    print("X",end='\t')
    for i in range(1,num+1):
        print(i,end='\t')
    print()
    for i in range(1,num+1):
        print(i,end='\t')
        
        for k in range(1,num+1):
            print(i*k,end='\t')
        print()
except ValueError as err:
    print("   Incorrect Input :"+str(err))
