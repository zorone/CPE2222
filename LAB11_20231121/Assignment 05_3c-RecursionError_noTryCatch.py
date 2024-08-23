from sys import getrecursionlimit

def recursivePrint(val :int):
    if(val > 0):
        recursivePrint(val-1)
    elif(val < 0):
        recursivePrint(val+1)
    print(val)

val = int(input('Enter value:'))
limit = getrecursionlimit()
if(val >= limit):
    print('Escaping RecursionError')
    print("Set val to {} so it won't exceed recursion limit.".format(limit-5))
    val = limit-5

recursivePrint(val)