from random import randint
generated_num=randint(1000000,9999999)
print('---------------Welcome To Bagel Game------------------')
for _ in range(7):
    num=int(input("Enter a 7 digits number: "))
    if len(str(num))==7:
        if num==generated_num:
            print('---------------Congragulation--You Won------------------')
            break
        for i in str(num):
            if i in str(generated_num):
                if str(num).index(i)==str(generated_num).index(i):
                    print("Fermi",end=' ')
                if(str(num).index(i)!=str(generated_num).index(i)):
                    print("Pico",end=' ')
            else:
                print("Bagels",end=' ')
        print()
        print('---------------Trial Left-{}------------------'.format(7-(_+1)))
        print(generated_num)
    else:
        print("check Your Digit Length")
print('---------------Game Over------------------')
