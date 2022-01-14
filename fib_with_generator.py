def fun():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for i in fun():
    if i>150:
        break
    print(i)
        
