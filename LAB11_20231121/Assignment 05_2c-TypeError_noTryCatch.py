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
            return (False, False) # string
    else:
        return (False, False) # Empty String

    if(count == 0):
        return (True, True) # int
    else:
        return (True, False) # float

xTest = testDecimal(x)
yTest = testDecimal(y)

if(mode == '+'):
    if(xTest[0] and yTest[0]):
        x = float(x)
        y = float(y)
    res = x + y

elif(mode == '*'):
    if(yTest[1] == True):
        y = int(y)
        res = x*y
    elif(xTest[0] and yTest[0]):
        x = float(x)
        y = float(y)
        res = x*y
    else:
        res = 'Escaping TypeError'
elif(xTest[0] and yTest[0]):
        x = float(x)
        y = float(y)
        if(mode == '-'):
            res = x - y
        elif(mode == '/'):
            res = x / y
        else:
            res = ('Operation is unavailable.')
else:
    res = 'Escaping TypeError'
print(res)