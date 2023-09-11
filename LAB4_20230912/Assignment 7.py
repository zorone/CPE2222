def multiplyMatrix(A, B):
    m = len(A)
    n = len(A[0])
    if(n != len(B)):
        return -1
    p = len(B[0])
    for (i, iVal) in enumerate(A):
        sum = 0
        
        for (j, jVal) in enumerate(B):
            sum += A[]