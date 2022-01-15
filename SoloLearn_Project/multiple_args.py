def concatenate(*args):
    concatnated=''
    for word in args:
        if args.index(word)!=len(args)-1:
            concatnated+=word+'-'
        else:
            concatnated+=word
    return concatnated
    

print(concatenate("I", "love", "Python", "!"))
