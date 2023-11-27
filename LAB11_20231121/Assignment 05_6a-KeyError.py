d = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
    d.setdefault(c, c)

print(d)