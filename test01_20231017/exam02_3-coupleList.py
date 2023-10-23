n = int(input("Please Enter Degree: "))

sz = 0
arrList = [[1], [1, 2]]
major = 1
minor = 0

for i in range(1, n+1):
    major = minor
    minor = not minor
    arrList[major] = list()
    sz += 1
    for j in range(0, sz+1):
        if j == 0:
            val = arrList[minor][-1]
        else:
            val = arrList[major][j-1] + arrList[minor][j-1]
        arr += [val]
    arrList += [arr]

res = arrList[major]
print(res)