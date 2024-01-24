# 5 * 5 matrix
# r * c matrix
# 5 rows
# 5 columns

# for i in range(1, 26):
#     print("*", end=" ")
#     if i % 5 == 0:
#         print()

# for i in range(1, 26):
#     print("{:2d}".format(i), end=" ")
#     if i % 5 == 0:
#         print()

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

for i in range(1, 6):
    # print(str(i) * 5)
    print(f"{i} " * 5)
print()

c = 1

for i in range(1, 26):
    print(c, end=" ")
    if i % 5 == 0:
        print()
        c += 1

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# c = 1

# for i in range(1, 26):
#     print(c, end=" ")
#     c += 1
#     if i % 5 == 0:
#         print()
#         c = 1
