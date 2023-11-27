from sys import getrecursionlimit

def recursivePrint(val :int):
    if(val > 0):
        recursivePrint(val-1)
    elif(val < 0):
        recursivePrint(val+1)
    print(val)

val = int(input('Enter value:'))
limit = getrecursionlimit()
print(limit)
if(val >= limit):
    print('Escaping RecursionError')
    print("Set val to {} so it won't exceed recursion limit.".format(limit))
    val = limit-1

recursivePrint(val)