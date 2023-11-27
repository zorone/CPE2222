a = list()
b = 0
for i in range(0, 100):
    if(i < 50):
        if(i%2 == 0):
            a += [i]
        else:
            b += i
    else:
        if(i%3 == 0):
            a += b
        else:
            b += a
    print(a)
    print(b)