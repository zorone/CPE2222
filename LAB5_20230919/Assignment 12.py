acceptRange = range(1, 40)
s = str()
romanDict = dict()

for i in range(1, 40):
    res, mod = divmod(i, 10)
    s = "X"*res
    
    if(mod == 9):
        s += "IX"
        
    elif(mod == 4):
        s += "IV"
        
    else:
        res, mod = divmod(mod, 5)
        s += "V"*res
        s += "I"*mod
    
    romanDict.update({i: s})
    
# print(romanDict)


while True:
    x = int(input("Enter a number for roman number conversion:"))
    
    if x not in acceptRange: break

    print('The roman number of {} is " {} "'.format(x, romanDict[x]))
    
    