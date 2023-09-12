acceptRange = range(1, 40)
s = str()

while True:
    x = int(input("Enter a number for roman number conversion:"))
    
    if x not in acceptRange: break
    
    res, mod = divmod(x, 10)
    s = "X"*res
    
    if(mod == 9):
        s += "IX"
        
    elif(mod == 4):
        s += "IV"
        
    else:
        res, mod = divmod(mod, 5)
        s += "V"*res
        s += "I"*mod

    print('The roman number of {} is " {} "'.format(x, s))
    
    