plaintext = input("Enter your plaintext (Alphabet Only):")
secretkey = int(input("Enter your secret key (Number Only):"))

upperList = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowerList = tuple('abcdefghijklmnopqrstuvwxyz')

def encrypt(P,k):
    for p in P:    
        if(p in upperList):
            temp = upperList.index(p)
            return upperList[(temp+k)%26]
        else:
            temp = lowerList.index(p)
            return lowerList[(temp+k)%26]  
    
def decrypt(C,k):
    for c in C:
        if(c in upperList):
            temp = upperList.index(c)
            return upperList[(temp-k)%26]
        else:
            temp = lowerList.index(c)
            return lowerList[(temp-k)%26]
    
ciphertext = encrypt(plaintext,secretkey)
print('The encrypted ciphertext:',ciphertext,sep='')
decryptedtext = decrypt(ciphertext,secretkey)
print('The decryption results:',decryptedtext,sep='')