pageBreak = "-"*50
Item = tuple()
Price = tuple()
Amount = tuple()

Item += str(input("Enter The 1st Product Name:"))
Price += float(input("Enter Price of Product:"))
Amount += int(input("Enter Quantity of Product:"))

Item += str(input("Enter The 2nd Product Name:"))
Price += float(input("Enter Price of Product:"))
Amount += int(input("Enter Quantity of Product:"))

Item += str(input("Enter The 3rd Product Name:"))
Price += float(input("Enter Price of Product:"))
Amount += int(input("Enter Quantity of Product:"))

print(pageBreak)
print("Inventory".center(50))
print(pageBreak)
print("Item".center(30), "Price".center(10), "Quantity".center(10))
print(pageBreak)

for i in range(3):
    print("{0}{1}{2}".format(0=Item[i].ljust(30), 1=Price[i].center(7), 2=Amount[i].rjust(13)))
    Total += Amount[i]

print(pageBreak)
print("Total Quantity = {}".format(Total))
print(pageBreak)