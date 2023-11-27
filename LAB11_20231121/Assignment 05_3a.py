def recursivePrint(val :int):
    if(val > 0):
        recursivePrint(val-1)
    elif(val < 0):
        recursivePrint(val+1)
    print(val)

input = int('Enter value:')
recursivePrint(input)