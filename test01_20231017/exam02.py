n = int(input("Please Enter Degree: "))
arr = list()

for i in range(0, n+2):
    if(i == -2):
        arr[0] = [1]
    elif(i == -1):
        arr[1] = [1, 1]
    else:
        arr[i+2] = [1]
        for j in range(len(arr[i+1])-1):
            val = arr[i+1][j] + arr[i+1][j+1]
            arr[i+2] += [val]
    print(arr[i])