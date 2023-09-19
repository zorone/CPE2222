def nthDegreePascal(re :int, *listVal):
    if(re <= 1):
        pascalList = [1, 1][0:re+1]
        return pascalList
    
    nthDegreePascal(re-1, listVal)
    
