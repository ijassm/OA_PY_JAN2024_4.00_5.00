def recursiveFunc(a):
    if a > 0:
        recursiveFunc(a - 1)
    print("Recursive function", a)


recursiveFunc(10)
