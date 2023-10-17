n = int(input("Please Enter Degree: "))

arr = [1]

for i in range(0, n):
    for j in range(0, n+1):
        if(j == 0):
            sz = len(arr)
            arr[j] = arr[sz-1]
        
        