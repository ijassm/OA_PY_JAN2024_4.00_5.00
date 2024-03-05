arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def double(arr):
#     output = []
#     for i in arr:
#         logic = i * 2
#         output.append(logic)
#     return output


# def triple(arr):
#     output = []
#     for i in arr:
#         logic = i * 3
#         output.append(logic)
#     return output


# print(double(arr))
# print(triple(arr))


# def double(i):
#     return i * 2

# double = lambda i : i * 2
# triple = lambda i : i * 3


# def triple(i):
#     return i * 3


def hof(arr, logicFunc):
    output = []
    for i in arr:
        output.append(logicFunc(i))
    return output


print(hof(arr, lambda i: i * 2))
print(hof(arr, lambda i: i * 3))
