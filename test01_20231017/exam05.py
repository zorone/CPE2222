pageBreak = "*"*35

print(pageBreak)
price = int(input("The total price of products: "))
pay = int(input("Customer payment: "))
print(pageBreak)

moneySize = (500, 100, 50, 20, 10, 5, 2, 1)

if(price == pay):
    print("Complete payment")
elif(price > pay):
    print("!!! Incorrect payment !!!")
else:
    print("List of money return")
    
    receipt = pay - price
    tempLeft = receipt
    tempAmount = 0
    
    for size in moneySize:
        tempAmount = int(tempLeft/size)
        if size > 10:
            text1 = "Banknote"
            text2 = "Piece"
        else:
            text1 = "Coin"
            text2 = "Coin"
        if tempAmount:
            tempLeft = tempLeft%size
            print("The {}-$Baht {} = {} {}(s)".format(size, text1, tempAmount, text2))