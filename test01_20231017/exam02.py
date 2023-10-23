n = int(input("Please Enter Degree: "))

arr = [1]
arrList = list()
arrList += arr

for i in range(1, n+1):
    arr = list()
    arr += [1]
    sz = len(arr)
    for j in range(0, n):
        print("{} {}: {}\n{} {}: {}".format(j, type(arrList[arr-1][j]), arrList[arr-1][j], j+1, type(arrList[arr-1][j+1], arrList[arr-1][j+1])))
        val = arrList[arr-1][j] + arrList[arr-1][j+1]
        arr += [val]
    arr += [1]
    arrList += arr

print(arrList)