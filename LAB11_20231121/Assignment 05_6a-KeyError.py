d = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
    cmd = "d.setdefault({}, '{}')".format(c, c)
    codeObj = compile(cmd, 'temp', 'exec')
    exec(codeObj)

print(d)