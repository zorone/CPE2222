d = dict()

try:
    for c in 'abcdefghijklmnopqrstuvwxyz':
        d[c] = c

    print(d)

    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(d[c])

except KeyError:
    print('Escaping KeyError')