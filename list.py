# even1 = 2
# even2 = 4

# [] = > list

# even = [2, 4, 6, 8, 10, 12, 12, 12]

# accessing index
# print("positive index values")
# print(even[0], "even[0]")
# print(even[1], "even[1]")
# print(even[2], "even[2]")
# print(even[3], "even[3]")
# print(even[4], "even[4]\n")

# print("negative index values")
# print(even[-1], "even[-1]")
# print(even[-2], "even[-2]")
# print(even[-3], "even[-3]")
# print(even[-4], "even[-4]")
# print(even[-5], "even[-5]")

# mutable
# print(even, "before")

# even[0] = 14

# print(even, "after")
# print(type(even))

# list methods

# print(even, "before")

# append - Adds an element at the end of the list
# even.append(16)

# clear - Removes all the elements from the list

# even.clear()

# copy - Returns a copy of the list

# a = even
# b = even.copy()
# c = even

# c[0] = 18

# print(a, "a")
# print(b, "b")
# print(c, "c")
# print(even, "even")

# print(id(a))
# print(id(b))
# print(id(c))
# print(id(even))


# count()	Returns the number of elements with the specified value

# print(even.count(12))

# a = [1, 2, 3]
# b = [4, 5, 6]

# a.extend(b)

# print(a)

# https://www.w3schools.com/python/python_ref_list.asp

# l = [2, 4, 1, 3, 5, 6]
# even = []
# odd = []

# for i in l:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even, "even")
# print(odd, "odd")

l = [2, 41, 85, 22, 12, 35, 5, 6]

length = len(l)

# sorting
# i = 2
# 2 > 4 => False [2, 4, 1, 3, 5, 6]
# 2 > 1 => True [1, 4, 2, 3, 5, 6]
# 1 > 3 => False [1, 4, 2, 3, 5, 6]
# 1 > 5 => False [1, 4, 2, 3, 5, 6]
# 1 > 6 => False [1, 4, 2, 3, 5, 6]

# i = 4
# 4 > 2 => True [1, 2, 4, 3, 5, 6]
# 2 > 3 => False [1, 2, 4, 3, 5, 6]
# 2 > 5 => False [1, 2, 4, 3, 5, 6]
# 2 > 6 => False [1, 2, 4, 3, 5, 6]

# i = 4
# 4 > 3 => True [1, 2, 3, 4, 5, 6]
# 3 > 5 => False [1, 2, 3, 4, 5, 6]
# 3 > 6 => False [1, 2, 3, 4, 5, 6]

# i = 4
# 4 > 5 => False [1, 2, 3, 4, 5, 6]
# 4 > 6 => False [1, 2, 3, 4, 5, 6]

# i = 5
# 5 > 6 => False [1, 2, 3, 4, 5, 6]


# for i in range(length - 1):
#     for j in range(i + 1, length):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]

# print(l)

# n = 5
# arr = [15, 2, 3, 4, 7, 6]
# length = len(arr)
# output = []

# for i in range(1, length + 1):
#     value = arr[i - 1]
#     if value == i:
#         output.append(value)

# print(output)
