plaintext = input("Enter your plaintext (Alphabet Only):")
secretkey = int(input("Enter your secret key (Number Only):"))

upperList = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowerList = tuple('abcdefghijklmnopqrstuvwxyz')

def encrypt(P,k):
    if(P in upperList):
        k += upperList.index(P)
        return upperList[k%26]
    else:
        k += lowerList.index(P)
        return lowerList[k%26]  
    
def decrypt(C,k):
    if(C in upperList):
        k -= upperList.index(C)
        return upperList[k%26]
    else:
        k -= upperList.index(C)
        return upperList[k%26]
    
ciphertext = encrypt(plaintext,secretkey)
print('The encrypted ciphertext:',ciphertext,sep='')
decryptedtext = decrypt(ciphertext,secretkey)
print('The decryption results:',decryptedtext,sep='')