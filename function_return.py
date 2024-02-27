a = [2, 3, 4, 5, 6]
b = [1, 2, 3, 4, 5]
s = []
p = 1


# def sum(l):
#     output = 0
#     for i in l:
#         output += i
#     s.append(output)


# def product(l):
#     global p
#     output = 1
#     for i in l:
#         output *= i
#     p = output


# print(sum(a))
# print(sum(b))

# product(s)

# print(s, "Sum")
# print(p, "Product")

# --------------------------
# with return


def sum(l):
    output = 0
    for i in l:
        output += i
    return output


print(sum(a) * sum(b))
