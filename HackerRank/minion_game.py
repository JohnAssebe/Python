def minion_game(string): 
    vowels='AEIOUaeiou'
    kevin_counter=0
    stuart_counter=0
    for i in range(len(string)):
        if s[i] in vowels:
            kevin_counter+=len(string)-i
        if s[i] not in vowels:
            stuart_counter+=len(string)-i
        
    if kevin_counter>stuart_counter:
        print("Kevin "+str(kevin_counter))
    elif(stuart_counter>kevin_counter):
        print("Stuart "+str(stuart_counter))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
