plaintext = input("Enter your plaintext (Alphabet Only):")
secretkey = int(input("Enter your secret key (Number Only):"))

upperList = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowerList = tuple('abcdefghijklmnopqrstuvwxyz')

def encrypt(P,k):
    encryptText = str()
    for p in P:    
        if(p in upperList):
            temp = upperList.index(p)
            encodeText += upperList[(temp+k)%26]
        else:
            temp = lowerList.index(p)
            encodeText += lowerList[(temp+k)%26]  
    
def decrypt(C,k):
    decryptText = str()
    for c in C:
        if(c in upperList):
            temp = upperList.index(c)
            decryptText += upperList[(temp-k)%26]
        else:
            temp = lowerList.index(c)
            decryptText += lowerList[(temp-k)%26]
    
ciphertext = encrypt(plaintext,secretkey)
print('The encrypted ciphertext:',ciphertext,sep='')
decryptedtext = decrypt(ciphertext,secretkey)
print('The decryption results:',decryptedtext,sep='')