try:
    cmd = "for i in range(1, 101)\n\tprint(i)"
    codeObj = compile(cmd, 'test', 'exec')
    exec(codeObj)
except SyntaxError:
    print('Escaping SyntaxError')