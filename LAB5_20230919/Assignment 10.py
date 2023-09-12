import sys

password = str((input("Setting your password:")))

tokenNegative = (" contain ", " not contain ")
tokenAmount = ("at least ", "more than ")
tokenType = ("capital ", "lowercase ", "8 ", "16 ")
tokenQuantifier = ("letter", "number", "characters")
header = "!!!ERROR!!! The password must"
s = str()

l = len(password)

if l < 8:
    s = header+tokenNegative[1]+tokenAmount[0]+tokenType[2]+tokenQuantifier[2]
elif l > 16:
    s = header+tokenNegative[1]+tokenAmount[0]+tokenType[2]+tokenQuantifier[2]
    
if len(s) > 0:
    print(s)
    sys.exit

for c in password:
    