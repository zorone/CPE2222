def recursive(size, *arr):
    if(size>2):
        arr = recursive(size-1, *arr)
        sz = len(arr)
        val = arr[sz-3] + 2*arr[sz-2] + 4*arr[sz-1]
        arr += (val, )
    elif(size == 2):
        arr = (1, 2, 3)
    elif(size == 1):
        arr = (1, 2)
    else:
        arr = (1, )

    return arr

arr = tuple()

n = int(input("Enter 'n' of Integer Sequence:"))
print("A tuple of Integer Sequence [n={}] is {}".format(n, recursive(n, arr)))