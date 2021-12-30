def transition_cipher(plain_text,key):
    cipher_text=['']*key
    for i in range(key):
        current_index=i
        while current_index<len(plain_text):
            cipher_text[i]+=plain_text[current_index]
            current_index+=key
    return ''.join(cipher_text)
print(transition_cipher('Common sense is not so common',8))
