pageBreak = "-"*50
Total = 0

Item = list()
Price = list()
Amount = list()

Item.append(str(input("Enter The 1st Product Name:")))
Price.append(float(input("Enter Price of Product:")))
Amount.append(int(input("Enter Quantity of Product:")))

Item.append(str(input("Enter The 2nd Product Name:")))
Price.append(float(input("Enter Price of Product:")))
Amount.append(int(input("Enter Quantity of Product:")))

Item.append(str(input("Enter The 3rd Product Name:")))
Price.append(float(input("Enter Price of Product:")))
Amount.append(int(input("Enter Quantity of Product:")))

print(pageBreak)
print("Inventory".center(50))
print(pageBreak)
print("{I}{P}{A}".format(I="Item".center(30), P="Price".center(10), A="Quantity".center(10)))
print(pageBreak)

for i in range(3):
    print("%30s%7f%13d"%(Item[i], Price[i], Amount[i]))
    Total += Amount[i]

print(pageBreak)
print("Total Quantity = {}".format(Total).rjust(50))
print(pageBreak)