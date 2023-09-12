import sys

password = str((input("Setting your password:")))

tokenNegative = (" contain ", " not contain ")
tokenAmount = ("at least", "more than")
tokenArticle = (" a ", " ")
tokenType = ("capital ", "lowercase ", "8 ", "16 ")
tokenQuantifier = ("letter", "number", "characters")
header = "!!!ERROR!!! The password must"

upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"

checkers = str("000")

s = str()

l = len(password)

if l < 8:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[1]+tokenType[2]+tokenQuantifier[2]
elif l > 16:
    s = header+tokenNegative[1]+tokenAmount[1]+tokenArticle[1]+tokenType[3]+tokenQuantifier[2]
    
if len(s) > 0:
    print(s)
    sys.exit(0)

for c in password:
    if(checkers[0] == "0"): 
        if c in upperCase:
            checkers[0] = "1"
    if(checkers[1] == "0"):
        if c in lowerCase:
            checkers[1] = "1"
    if(checkers[2] == "0"):
        if c in number:
            checkers[2] = "1"

if(checkers[0] == "0"):
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenType[0]+tokenQuantifier[0]
elif(checkers[1] == "0"):
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenType[1]+tokenQuantifier[0]
elif(checkers[2] == "0"):
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenQuantifier[0]
else:
    s= ":-) Your password is correct (-:"
    
print(s)