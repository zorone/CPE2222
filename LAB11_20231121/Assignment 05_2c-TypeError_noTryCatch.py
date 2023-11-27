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
            return False
    return True

if(mode == '+'):
    res = x + y

elif(testDecimal(y)):
    if(mode == '*'):
        res = x*y
    elif(testDecimal(x)):
        if(mode == '-'):
            res = x - y
        elif(mode == '/'):
            res = x / y
        else:
            res = ('Operation is unavailable.')
    else:
        res = 'Escaping TypeError'
else:
    res = 'Escaping TypeError'
print(res)