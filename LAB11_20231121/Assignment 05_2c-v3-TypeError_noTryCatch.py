x = input("Enter first argument:")
y = input("Enter second argument:")
print("Usable modes: +, -, *, /")
mode = input("Please enter modes:")

def testDecimal(data):
    count = 0
    for s in data:
        if(s in '0123456789'):
            continue
        elif(s in '.' and count < 1):
            count += 1
        else:
            return data, (False, False) # string
    else:
        if(len(data) == 0):
            return data, (False, False) # Empty String

    if(count == 0):
        data = int(data)
        return data, (True, True) # int
    else:
        data = float(data)
        return data, (True, False) # float

x, xTest = testDecimal(x)
y, yTest = testDecimal(y)

if(mode == '+'):
    res = x + y

elif(mode == '*'):
    if((xTest[0] and yTest[0]) or (yTest[1] == True)):
        res = x*y
    else:
        res = 'Escaping TypeError'
elif(xTest[0] and yTest[0]):
        if(mode == '-'):
            res = x - y
        elif(mode == '/'):
            res = x / y
        else:
            res = ('Operation is unavailable.')
else:
    res = 'Escaping TypeError'
print(res)