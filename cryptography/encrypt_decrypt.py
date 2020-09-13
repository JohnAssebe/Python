'''@Author:Yohannes Assebe'''
from cryptography.fernet import Fernet
#first import the module
def generate_key():
    #this function generate key to encrypt the file
    key=Fernet.generate_key()
    with open("key.txt",'wb') as file:
        #write the key to key.txt file
        file.write(key)
def read_file():
    #this function reads the key and display to console
    with open('key.txt','rb') as file:
        return file.read()
generate_key()
key=read_file()
#initialize a fernet key
f=Fernet(key)
word="This is John Assebe"
def encrypt_file():
    #encode method used to convert str into byte
    encrypted_word=f.encrypt(word.encode())
    return encrypted_word 
def decrypt_file(encrypted_word):
    return f.decrypt(encrypted_word)
encrypted=encrypt_file()
print("\tEncrypted Word :\n")
print(encrypted.decode())
#to convert into string format we decode it 
print()
print("\tDecrypted Word:\n")
print(decrypt_file(encrypted).decode())#convert byte to string



