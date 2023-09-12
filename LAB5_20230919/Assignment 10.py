password = str((input("Setting your password:")))

tokenNegative = (" ", " not ")
tokenAmount = ("at least ", "more than ")
tokenQuantifier = ("letter", "number", "characters")
header = "!!!ERROR!!! The password must"

l = len(password)

if l < 8:
    s = header+tokenNegative[1]+"contain "+tokenAmount[0]+"8"+tokenQuantifier[2]
    print(s)

for c in password:
    