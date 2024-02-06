a = "hello"

# immutable object
# a[0] = "e"
# print(a[0], "a[0]")

# iterator

# for i in a:
#     print(i)

# 1. Given a non-empty sequence of characters str, return true if sequence is Binary, else return false

# a = "101"
# output = ""

# for i in a:
#     if i != "0" and i != "1":
#         output = 0
#         break
#     output = 1

# print(output)

# 2.Given a string, remove spaces from it.

# s = "geeks  for         geeks"

# output = ""

# for i in s:
#     if i != " ":
#         output += i

# print(output)


# Given a string S. The task is to convert characters of string to lowercase.

s = "ABCDdE"

# print(ord("A"))
# print(s.lower())

output = ""

for i in s:
    if ord(i) >= 64 and ord(i) <= 90:
        capsCharLowerValue = ord(i) + 32
        output += chr(capsCharLowerValue)
        # print(capsCharLowerValue, f": {chr(capsCharLowerValue)}")
    else:
        output += i

print(s, "before conversion")
print(output, "after conversion")
