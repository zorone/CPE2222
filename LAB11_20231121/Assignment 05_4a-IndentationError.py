cmd = "for i in range(1, 101):\nprint(i)"
codeObj = compile(cmd, 'test', 'exec')
exec(codeObj)