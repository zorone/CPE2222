n = int(input("Please Enter Degree: "))

sz = 1
arrList = [[1], [1, 2]]
major = 1
minor = 0

for i in range(2, n+1):
    major = minor
    minor = (minor+1)%2
    sz += 1
    for j in range(sz+1, 0, -1):
        if j == 0:
            arrList[major][j] = arrList[minor][-1]
        elif j < sz-1:
            arrList[major][j] = arrList[major][-j] + arrList[minor][-j]
        else:
            arrList[major] += [arrList[major][-j] + arrList[minor][-j]]

if(n < 2):
    res = arrList[n]
else:
    res = arrList[major]
print(res)