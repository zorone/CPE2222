x = input("Enter first argument:")
y = input("Enter second argument:")
print("Usable modes: +, -, *, /")
mode = input("Please enter modes:")

res = int()

if(mode == '+'):
    cmd = 'res = x + y'
    codeObj = compile(cmd)
elif(mode == '-'):
    cmd = 'res = x - y'
    codeObj = compile(cmd)
elif(mode == '*'):
    cmd = 'res = x * y'
    codeObj = compile(cmd)
elif(mode == '/'):
    cmd = 'res = x / y'
    codeObj = compile(cmd)
else:
    print('Operation is unavailable.')
try:
    exec(codeObj)
    print(res)
except TypeError:
    print("Escaping TypeError")