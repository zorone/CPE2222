n = int(input("Please Enter Degree: "))

sz = 0
arr = [1]
arrList = list()
arrList += [arr]

for i in range(1, n+1):
    arr = list()
    arr += [1]
    sz = len(arrList)
    for j in range(0, sz-1):
        if sz < 2:
            arr = [1, 2]
            arrList += [arr]
            continue
        if j == 0:
            val = arrList[sz-1][sz-1]
        else:
            val = arrList[sz-1][j-1] + arr[j-1]
        arr += [val]
    arr += [1]
    arrList += [arr]

print(arrList)
res = arrList[sz]
print(res)