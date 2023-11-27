x = input("Enter first argument:")
y = input("Enter second argument:")
print("Usable modes: +, -, *, /")
mode = input("Please enter modes:")

if(mode == '+'):
    res = x + y
elif(mode == '-'):
    res = x - y
elif(mode == '*'):
    res = x * y
elif(mode == '/'):
    res = x/y
else:
    print('Operation is unavailable.')
print(res)