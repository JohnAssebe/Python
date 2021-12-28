'''
@author Yohannes Assebe
This program works a shift ceaser encryption and decryption for alphabets only'Broken Vessels (Amazing Grace) [Official Lyric Video] - Hillsong Worship.mp4'
It is easy to crack ceasar cipher to crack so don't use for stritly secret message easily broken using brute force
'''
def caesar_cipher(shift,text,mode=0):
    if shift>26:
        return """please enter a valid shift value"""
    alphabet_list=['A','B','C','D','E','F','G','H','I',
                   'J','K','L','M','N','O','P','Q','R',
                   'S','T','U','V','W','X','Y','Z']
    shifted_alphabet=[]
    encrypted_text=''
    decrypted_text=''
    if mode==0:
        for i in range(len(alphabet_list)):
            shift_value=shift+i
            if(shift_value>25):
                shift_value=(shift+i)-26
            shifted_alphabet.append(alphabet_list[shift_value])
            
        for i in range(len(text)):
            try:
                text_letter_index=alphabet_list.index(text.upper()[i])
                encrypted_text=encrypted_text+shifted_alphabet[text_letter_index]
            except:
                encrypted_text=encrypted_text+text[i]
                
        return encrypted_text
    elif mode==1:
        for i in range(len(text)):
             try:
                 text_letter_index=alphabet_list.index(text.upper()[i])
                 decrypted_text=decrypted_text+alphabet_list[text_letter_index-shift]
             except:
                 decrypted_text=decrypted_text+text[i]
        return decrypted_text
        
    else:
        return '''Mode value must be 0 or 1,
                  0=>To Encrypt
                  1=>To Decrypt
                  Example=>caesar_cipher(15,"JOHN Assebe Square",0);
                           caesar_cipher(15,"YDWC PHHTQT HFJPGT",1);
               '''
        
if __name__=='__main__':
    text=input("Enter A text to encrypt or decrypt: ")
    shift=int(input("Enter shift value which must be between 0 and 26: "))
    mode=int(input("Enter 0 to encrypt or 1 to decrypt: "))
    print(caesar_cipher(shift,text,mode))
    
#print(caesar_cipher(15,"JOHN Assebe Square",0));
#print()
#print(caesar_cipher(15,"YDWC PHHTQT HFJPGT",1))
    
    
