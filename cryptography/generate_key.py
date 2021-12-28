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
print("The Generated Key: "+str(read_file()))
