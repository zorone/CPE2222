n = int(input("Please Enter Degree: "))

sz = 0
arr = [1]
arrList = list()
arrList += [arr]

for i in range(1, n+1):
    sz += 1
    arr = list()
    for j in range(0, sz+1):
        if j == 0:
            val = arrList[-1][-1]
        else:
            val = arrList[-1][-1] + arr[-1]
        arr += [val]
    arrList += [arr]

res = arrList[sz]
print(res)