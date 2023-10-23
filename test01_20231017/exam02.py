n = int(input("Please Enter Degree: "))

arr = [1]
arrList = list()
arrList += [arr]

for i in range(1, n+1):
    arr = list()
    arr += [1]
    sz = len(arrList)
    for j in range(0, sz):
        if sz < 2:
            continue
        print("{} {}: {}\n{} {}: {}".format(j, type(arrList[sz-1][j]), arrList[sz-1][j], j+1, type(arrList[sz-1][j+1], arrList[sz-1][j+1])))
        val = arrList[sz-1][j] + arrList[sz-1][j+1]
        arr += [val]
    arr += [1]
    arrList += arr

print(arrList)