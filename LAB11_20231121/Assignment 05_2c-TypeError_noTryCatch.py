x = input("Enter first argument:")
y = input("Enter second argument:")
print("Usable modes: +, -, *, /")
mode = input("Please enter modes:")

if(mode == '+'):
    res = x + y
elif(testDecimal(y)):
    if(mode == '*'):
        res = x*y
elif(x.isdigit):
elif(mode == '-'):
    res = x - y
elif(mode == '/'):
    res = x/y
else:
    print('Operation is unavailable.')
print(res)

def testDecimal(str):
    for s in