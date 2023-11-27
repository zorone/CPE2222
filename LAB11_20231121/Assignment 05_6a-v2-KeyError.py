d = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
    cmd = "d.setdefault('{}', '{}')".format(c, c)
    codeObj = compile(cmd, 'temp', 'exec')
    exec(codeObj)

for c in 'abcdefghijklmnopqrstuvwxyz':
    cmd = "print(d[{}])".format(c)
    codeObj = compile(cmd, 'temp', 'exec')
    exec(codeObj)
