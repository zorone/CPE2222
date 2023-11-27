d = dict()
for c in 'abcdefghijklmnopqrstuvwxyz':
    d[c] = '{}'.format(c)

print(d)

for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(d[c])
