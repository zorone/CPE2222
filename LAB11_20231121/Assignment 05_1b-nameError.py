dup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# only show list of itself when data no less than 5; else show accumulate list until this iterations.

try:
    for data in dup:
        if(data >= 5):
            res = [data]
        else:
            res += [data]
    print(res)

except NameError:
    res = list()
    print("Escaping NameError")

finally:
    for data in dup:
        if(data >= 5):
            res = [data]
        else:
            res += [data]
    print(res)