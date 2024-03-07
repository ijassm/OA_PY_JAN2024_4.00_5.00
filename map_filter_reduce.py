import functools

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def hof(arr, logicFunc):
#     output = []
#     for i in arr:
#         output.append(logicFunc(i))
#     return output


# def myMap(arr, logicFunc):
#     return [logicFunc(i) for i in arr]


# myMap = lambda logicFunc, arr: [logicFunc(i) for i in arr]
# myFilter = lambda logicFunc, arr: [i for i in arr if logicFunc(i)]

# print(myMap(lambda i: i * 2, arr))
# print(myMap(lambda i: i * 3, arr))
# print(list(map(lambda i: i * 3, arr)))

# print(myFilter(lambda i: i % 2 == 0, arr))
# print(list(filter(lambda i: i % 2 == 0, arr)))

# print()


# def func(accumulator, currentValue):
#     print(accumulator, currentValue)
#     return 1


# functools.reduce(func, arr, 10)


# def func(accumulator, currentValue):
#     return accumulator + currentValue


# print(functools.reduce(lambda acc, cv: acc + cv, arr, 10))


def myReduce(cbFunc, arr, initialValue=None):
    for i in arr:
        if initialValue != None:
            initialValue = cbFunc(initialValue, i)
        else:
            initialValue = i

    return initialValue


print(myReduce(lambda acc, cv: acc + cv, arr, 10))
print(myReduce(lambda acc, cv: acc + cv, arr))
