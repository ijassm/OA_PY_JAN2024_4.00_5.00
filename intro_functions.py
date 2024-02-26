# Function Definition
# def abc():
#     print("Hello World!")


# print("welcome")

# # Function Call
# abc()
# abc()
# abc()

# print("bye")


l1 = [2, 3, 4, 5, 6]
l2 = [4, 34, 42, 53, 26]
l3 = [22, 36, 42, 56, 56]
l4 = [25, 32, 4, 523, 6]


# s1 = 0
# for i in range(len(l1)):
#     s1 += l1[i]
# print(s1, "s1")

# s2 = 0
# for i in range(len(l2)):
#     s2 += l2[i]
# print(s2, "s2")

# s3 = 0
# for i in range(len(l3)):
#     s3 += l3[i]
# print(s3, "s3")

# s4 = 0
# for i in range(len(l4)):
#     s4 += l4[i]
# print(s4, "s4")


# def sum(l):
#     s = 0
#     for i in range(len(l)):
#         s += l[i]
#     print(s, l)


# sum(l1)
# sum(l2)
# sum(l3)
# sum(l4)

string1 = "**Docoding123456789everyday##"
string2 = "**oceanacademy123##"


def splitString(s):
    s1 = ""
    s2 = ""
    s3 = ""

    for i in s:
        if i.isalpha():
            s1 += i
        elif i.isdigit():
            s2 += i
        else:
            s3 += i

    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            s1 += i
        elif ord(i) >= 48 and ord(i) <= 57:
            s2 += i
        else:
            s3 += i

    print(s1, "s1")
    print(s2, "s2")
    print(s3, "s3")


splitString(string1)
splitString(string2)
