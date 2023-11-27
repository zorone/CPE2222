from sys import getrecursionlimit

def recursivePrint(val :int):
    if(val > 0):
        recursivePrint(val-1)
    elif(val < 0):
        recursivePrint(val+1)
    print(val)

val = int(input('Enter value:'))

if(val > getrecursionlimit()):
    print('Escaping RecursionError')
    
try:
    recursivePrint(val)
except RecursionError:
    print('Escaping RecursionError')