def search4vowel(word:str)->set:
    vowels=set('aeiou')
    return vowels.intersection(set(word))

def search4letter(phrase:str,word:str='aeiou')->set:
    found=set(phrase).intersection(set(word))
    return found

