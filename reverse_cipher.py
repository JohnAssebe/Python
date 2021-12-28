'''
@author Yohannes Assebe
This program encrypt and decrypt a plain text by reversing
reverse cipher use the same encrypt and decrypt algorithm 
'''
def reverse_cipher(plain_text):
    length=len(plain_text)
    reversed_=''
    i=0
    while(i<length):
        reversed_=reversed_+plain_text[length-1-i]
        i=i+1
    return reversed_
        
if __name__=='__main__':
    plain_text=input('Enter A Text: ')
    print(reverse_cipher(plain_text))
    
   # encrypt a plain_text
# print('encrypt')
# print(reverse_cipher("John is the password"))
# print()
# print('decrypt')
   # decrypt an encrypted text
# print(reverse_cipher('drowssap eht si nhoJ'))
