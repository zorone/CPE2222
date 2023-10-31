def recursive(*arg):
    sz = len(arg)
    if(sz > 1):
        recursive(arg[0:sz-1])
    print(arg)
    
recursive("Hello World!")