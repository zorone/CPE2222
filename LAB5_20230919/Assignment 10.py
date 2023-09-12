import sys

password = str((input("Setting your password:")))

tokenNegative = (" contain", " not contain")
tokenAmount = ("at least ", "more than ")
tokenArticle = (" a ", " ")
tokenType = ("capital ", "lowercase ", "8 ", "16 ")
tokenQuantifier = ("letter", "number", "characters")
header = "!!!ERROR!!! The password must"

upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"

checkers = int(0)

s = str()

l = len(password)

if l < 8:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[1]+tokenType[2]+tokenQuantifier[2]
elif l > 16:
    s = header+tokenNegative[1]+tokenAmount[0]+tokenArticle[1]+tokenType[3]+tokenQuantifier[2]
    
if len(s) > 0:
    print(s)
    sys.exit

for c in password:
    if(checkers < 4): 
        if c in upperCase:
            checkers += 4
    if(checkers < 2):
        if c in lowerCase:
            checkers += 2
    if(checkers < 1):
        if c in number:
            checkers += 1

if(checkers < 4):
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[1]+tokenType[2]+tokenQuantifier[2]