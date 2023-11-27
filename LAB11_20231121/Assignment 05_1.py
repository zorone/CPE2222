dup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for data in dup:
    if(data < 5):
        res = [data]
    else:
        res += [data]

print(res)