x = input("Enter first argument:")
y = input("Enter second argument:")
print("Usable modes: +, -, *, /")
mode = input("Please enter modes:")

res = int()

if(mode == '+'):
    cmd = 'res = x + y'
    codeObj = compile(cmd, 'test', 'exec')
elif(mode == '-'):
    cmd = 'res = x - y'
    codeObj = compile(cmd, 'test', 'exec')
elif(mode == '*'):
    cmd = 'res = x * y'
    codeObj = compile(cmd, 'test', 'exec')
elif(mode == '/'):
    cmd = 'res = x / y'
    codeObj = compile(cmd, 'test', 'exec')
else:
    cmd = "print('Operation is unavailable.')"
    codeObj = compile(cmd, 'test', 'exec')
try:
    exec(codeObj)
    print(res)
except TypeError:
    print("Escaping TypeError")