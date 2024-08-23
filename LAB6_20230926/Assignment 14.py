def nthDegreePascal(re :int):
    pascalList = list()
    if(re <= 1):
        temp = [1, 1][0:re+1]
        return temp
    else:
        temp = nthDegreePascal(re-1)
    
    pascalList += [1]
    for i in range(0, len(temp)-1):
        pascalList += [temp[i]+temp[i+1]]
    
    pascalList += [1]
        
    return pascalList

n = int(input("Please Enter Degree of Pascal Triangle: "))
print(nthDegreePascal(n))