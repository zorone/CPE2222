plaintext = input("Enter your plaintext (Alphabet Only):")
secretkey = int(input("Enter your secret key (Number Only):"))

upperList = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowerList = tuple('abcdefghijklmnopqrstuvwxyz')

def encrypt(P,k):
    for p in P:    
        if(p in upperList):
            k += upperList.index(p)
            return upperList[k%26]
        else:
            k += lowerList.index(p)
            return lowerList[k%26]  
    
def decrypt(C,k):
    for c in C:
        k += 26
        if(c in upperList):
            k -= upperList.index(c)
            return upperList[k%26]
        else:
            k -= lowerList.index(c)
            return lowerList[k%26]
    
ciphertext = encrypt(plaintext,secretkey)
print('The encrypted ciphertext:',ciphertext,sep='')
decryptedtext = decrypt(ciphertext,secretkey)
print('The decryption results:',decryptedtext,sep='')