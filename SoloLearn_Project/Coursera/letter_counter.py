def count_letter(text):
    letters={}
    for letter in text:
        if letter not in letters:
            letters[letter]=0
        letters[letter]+=1
    return letters
print(count_letter("Yohannes Assebe"))
