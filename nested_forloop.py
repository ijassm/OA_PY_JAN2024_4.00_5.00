import math

# for i in range(1, 3):
#     for j in range(1, 3):
#         for k in range(1, 3):
#             print(i, j, k)

# i = 1
##### j = 1 | j = 2
# i = 2
##### j = 1 | j = 2

# i = 1
### j = 1
# k = 1 | k = 2
### j = 2
# k = 1 | k = 2
# i = 2
### j = 1
# k = 1 | k = 2
### j = 2
# k = 1 | k = 2


# for i in range(1, 6):
#     for j in range(1, 6):
#         print("*", end=" ")
#     print()


# The pattern like :

# *
# **
# ***
# ****
# n = 10

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()


# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

n = 5

# for i in range(1, n):
#     for j in range(1, 6):
#         print(j, end=" ")
#     print()

# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

# for i in range(1, n):
#     for j in range(5, 0, -1):
#         print(j, end=" ")
#     print()

# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25


# n = 5
# r = 0
# space = " " * 1


# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         r += 1
#         print("{:2d}".format(r), end=" ")
#     print()

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         r += 1
#         length = math.floor((math.log10(r)) + 1)
#         if length > 1:
#             print(r, end=space)
#         else:
#             print(f"{r} ", end=space)
#     print()


# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         r += 1
#         if len(str(r)) > 1:
#             print(r, end=space)
#         else:
#             print(f"{r} ", end=space)
#     print()


# 1  3  5  7  9
# 11 13 15 17 19
# 21 23 25 27 29
# 31 33 35 37 39
# 41 43 45 47 49

# n = 5
# r = 1

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print("{:2d}".format(r), end=" ")
#         r += 2
#     print()
