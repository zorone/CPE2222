d = dict()

try:
    for c in 'abcdefghijklmnopqrstuvwxyz':
        d[c] = c

    print(d)

    for c in 'abcdefghijklmnopqrstuvwxyz':
        print(d[c])

except KeyError:
    print('Escaping KeyError')