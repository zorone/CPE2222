import sys

password = str((input("Setting your password:")))

tokenNegative = (" contain ", " not contain ")
tokenAmount = ("at least", "more than")
tokenArticle = (" a ", " ")
tokenType = ("capital ", "lowercase ", "8 ", "16 ")
tokenQuantifier = ("letter", "number", "characters")
header = "!!!ERROR!!! The password must"

upperCase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowerCase = set("abcdefghijklmnopqrstuvwxyz")
number = set("0123456789")

l = len(password)

c = set(password)

if l < 8:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[1]+tokenType[2]+tokenQuantifier[2]
elif l > 16:
    s = header+tokenNegative[1]+tokenAmount[1]+tokenArticle[1]+tokenType[3]+tokenQuantifier[2]
elif len(upperCase.difference(c)) > 25:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenType[0]+tokenQuantifier[0]
elif len(lowerCase.difference(c)) > 25:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenType[1]+tokenQuantifier[0]
elif len(number.difference(c)) > 9:
    s = header+tokenNegative[0]+tokenAmount[0]+tokenArticle[0]+tokenQuantifier[1]
else:
    s= ":-) Your password is correct (-:"
    
print(s)