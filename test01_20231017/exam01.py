def recursive(size, *arr):
    if(size == 0):
        arr += (1, )
    else:
        if(size == 1):
            arr += (2, )
        elif(size == 2):
            arr += (3, )
        else:
            size = len(arr)
            val = arr[size-3] + 2*arr[size-2] + 4*arr[size-1]
            arr += (val, )
    
    return arr

n = int(input("Enter 'n' of Integer Sequence:"))