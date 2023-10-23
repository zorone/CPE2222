n = int(input("Please Enter Degree: "))

arr = [1]
arrList = list()
arrList += arr

for i in range(1, n):
    arr = list()
    arr += 1
    for j in range(0, n):
        if(j == 0):
            sz = len(arr)
            arr[j] = arr[sz-1]
    arr += 1
    arrList += arr