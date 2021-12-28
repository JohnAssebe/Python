'''@author Yohannes Assebe
Ceasar cipher easily decrypted by brute force
'''
def ceasar_cipher(plain_text,key):
     symbols='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz0123456789+=-_~!@#$%^&*()";:,. '
     encrypted_text=''
     for letter in plain_text:
         if letter in symbols:
             encrypted_index=symbols.find(letter)+key
             if(encrypted_index>len(symbols)):
                 encrypted_index=symbols.find(letter)+key-len(symbols)
             encrypted_text=encrypted_text+symbols[encrypted_index]
         else:
             encrypted_text=encrypted_text+letter;
     return encrypted_text

def brute_force_ceasar(encrypted_text):
    symbols='ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz0123456789+=-_~!@#$%^&*()";:,. '
    for i in range(len(symbols)):
        key=i
        plain_text=''
        for letter in encrypted_text:
            if letter in symbols:
                if symbols.find(letter)-key<0:
                    decrypt_key=symbols.find(letter)-key+len(symbols)
                decrypt_key=symbols.find(letter)-key
                plain_text=plain_text+symbols[decrypt_key]
            else:
                plain_text=plain_text+letter
        print("decrypt_key :%s , text :%s"%(key,plain_text))
print(ceasar_cipher('I Am Cool',15))
brute_force_ceasar('YOP2OR441')
