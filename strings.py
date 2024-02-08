# a = "hello"

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


# 3. Given a string S. The task is to convert characters of string to lowercase.

# s = "ABCDdE"

# # print(ord("A"))
# # print(s.lower())

# output = ""

# for i in s:
#     if ord(i) >= 64 and ord(i) <= 90:
#         capsCharLowerValue = ord(i) + 32
#         output += chr(capsCharLowerValue)
#         # print(capsCharLowerValue, f": {chr(capsCharLowerValue)}")
#     else:
#         output += i

# print(s, "before conversion")
# print(output, "after conversion")

# 4. Given a String S , print the reverse of the string as output.

# s = "ymedacanaeco"
# s = "malayalam"
# # print(s[::-1])
# output = ""
# length = len(s)

# for i in range(length - 1, -1, -1):
#     output += s[i]

# print(output)

# 5. Given a string str, convert the first letter of each word in the string to uppercase.

# str = "i love programming"
# l = str.split(" ")

# print(l)

# output = ""

# for i in l:
#     output += i[0].capitalize() + i[1:]

# print(output)


# 6. Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.

# s = "practice"
# vowels = []

# for i in s:
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#         print(i)


# 7. Given a string, check if all its characters are the same or not.

# s = "aaaaab"

# output = False
# length = len(s) - 1

# for i in range(length):
#     if s[i] == s[i + 1]:
#         output = True
#     else:
#         output = False
#         break

# print(output)


# 8. Given a string S as input. Delete the characters at odd indices of the string.

# s = "ocean"
# length = len(s)
# output = ""

# for i in range(length):
#     if i % 2 == 0:
#         output += s[i]

# print(output)

"""
9. Given a string S which consists of alphabets , 
numbers and special characters. 
You need to write a program to split the strings in three different 
strings S1, S2 and S3 such that the string S1 will contain all the 
alphabets present in S , the string S2 will contain all the numbers 
present in S and S3 will contain all special characters present in S.  
The strings S1, S2 and S3 should have characters in same order as they appear in input.
"""

# s = "**Docoding123456789everyday##"

# s1 = ""
# s2 = ""
# s3 = ""

# for i in s:
#     if i.isalpha():
#         s1 += i
#     elif i.isdigit():
#         s2 += i
#     else:
#         s3 += i

# for i in s:
#     if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
#         s1 += i
#     elif ord(i) >= 48 and ord(i) <= 57:
#         s2 += i
#     else:
#         s3 += i

# print(ord("1"))

# print(s1)
# print(s2)
# print(s3)


# 10. Given a string s, extract all the integers from s.

# s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
# output = ""

# for i in s:
#     if ord(i) >= 48 and ord(i) <= 57:
#         output += " " + i

# print(output)

"""
11. Given a string of a constant length, print a triangle out of it. 
The triangle should start with the given string and keeps shrinking downwards 
by removing one character from the begining of the string. The spaces on the 
left side of the triangle should be replaced with dot character.
"""

# s = "oceanacademy"
# length = len(s)
# output = ""

# for i in range(length):
#     output = "." * i + s[i:]
#     print(output)


"""
12. Given a string S, consisting only of english alphabets, 
replace all the alphabets with the alphabets occuring at the same 
position when counted in reverse order of alphabets. 
For example, 'a' would be replaced by 'z', 'b' by 'y', 'c' by 'x' 
and so on. Any capital letters would be replaced by capital letters only.
"""

# s = "hello"

# if(True):
#     pass
