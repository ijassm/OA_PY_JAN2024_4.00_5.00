# range(start,stop,step)
# range(3) => start - 0, stop - 3 , step - 1
# range(1,3) => start - 1, stop - 3 , step - 1
# range(1,3,2) => start - 1, stop - 3 , step - 2

# for i in range(3):
#     print("hello world", i)

# for i in range(1, 3):
#     print("hello world", i)

# for i in range(1, 11, 2):
#     print("hello world", i)

# for i in range(1, -5, -1):
#     print("hello world", i)

# for i in range(10, 0, -1):
#     print("hello world", i)

# i = 1
# i = 0
# i = -1
# i = -2
# i = -3
# i = -4

# # 1st loop
# i = 0
# # 2nd loop
# i = 1
# # 3rd loop
# i = 2

a = "oc ea n"
newString = ""
length = len(a)

# print(length)

# a[0] = "fdgn"

for i in range(length):
    if a[i] != " ":
        # print(a[i], i)
        # newString = newString + a[i]
        newString += a[i]

print(a)
print(newString)

# newString = ""

# i = 0
# a[i] => "o"
# newString = "" + "o"
# newString = "o"

# i = 1
# a[i] => "c"
# newString = "o" + "c"
# newString = "oc"

# i = 2
# a[i] => " "
# Condition False

# i = 3
# a[i] => "e"
# newString = "oc" + "e"
# newString = "oce"

# i = 4
# a[i] => "a"
# newString = "oce" + "a"
# newString = "ocea"

# i = 5
# a[i] => " "
# Condition False

# i = 6
# a[i] => "n"
# newString = "ocea" + "n"
# newString = "ocean"

