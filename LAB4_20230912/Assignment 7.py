def multiplyMatrix(A, B):
    m = len(A)
    n = len(A[0])
    if(n != len(B)):
        return -1
    p = len(B[0])
    
    res = tuple()
    
    for i in range(0, m):
        t_res = tuple()
        
        for j in range(0, p):
            sum = 0
            
            for k in range(0, n):
                sum += A[i][k] * B[k][j]
                 
            t_res += (sum, )
              
        res += (t_res, )
    
    return res

def transposeMatrix(A):
    n = len(A[0])
    
    res = tuple()
    
    for i in range(0, n):
        t_res = tuple()
        for eachRow in A:
            t_res += (eachRow[i], )
        res += (t_res, )
            
    return res

A = ((1, 3, 5), (2, 4, 6))
tA = transposeMatrix(A)
AtA = multiplyMatrix(A, tA)

starBreak = '*' * 90
pageBreak = '-' * 90

print(starBreak)
print("Matrix with Tuple".center(90))
print(starBreak)

x = int(input('Enter row number of the "A" matrix: '))
x -= 1
y = int(input('Enter column number of the "A" matrix: '))
y -= 1
print('The "a{x}{y}" element in the "A" matrix is {n}'.format(x=x, y=y, n=A[x][y]))

print(pageBreak)
x = int(input('Enter row number of the transposed "A" matrix: '))
x -= 1
y = int(input('Enter column number of the transposed "A" matrix: '))
y -= 1
print('The "b{x}{y}" element in the transposed "A" matrix is {n}'.format(x=x, y=y, n=tA[x][y]))

print(pageBreak)
x = int(input('Enter row number of multiplication of matrices "A" and transposed of "A": '))
x -= 1
y = int(input('Enter column number of multiplication of matrices "A" and transposed of "A": '))
y -= 1
print('The "c{x}{y}" element in multiplication of the "A" matrix and the transposed "A" matrix is {n}'.format(x=x, y=y, n=AtA[x][y]))

print("-".ljust(90, "-"))
