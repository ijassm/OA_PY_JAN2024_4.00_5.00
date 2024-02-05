# while condition:
#     pass

# a = 142

# i = 0

# while i < 10:
#     i += 1
#     print(i)


# 1. Write a python program to print all natural numbers from 1 to n. – using while loop

# n = int(input("Enter the n number: "))
# i = 0

# while i < n:
#     i += 1
#     print(i)

# 2.Write a python program to print all natural numbers in reverse (from n to 1). – using while loop

# n = int(input("Enter the n number: "))
# i = 1

# while n >= i:
#     print(n)
#     n -= 1

# 3.Write a python program to print all alphabets from a to z. – using while loop

# start = 97
# stop = 122

# # print(chr(97))

# while start != stop + 1:
#     print(chr(start))
#     start += 1

# 4.Write a python program to print all even numbers between 1 to 100. – using while loop

# i = 0
# stop = 100

# while i < stop:
#     i += 2
#     print(i)

# 5.Write a python program to print all odd number between 1 to 100.

# i = 1
# stop = 100

# while i < stop:
#     print(i)
#     i += 2

# 6. Write a python program to find sum of all natural numbers between 1 to n.

# i = 0
# sum = 0
# n = 10

# while i < n:
#     i += 1
#     sum += i

# print("sum =", sum)

# 7. Write a python program to find sum of all even numbers between 1 to n.

# i = 0
# evenSum = 0
# n = 10

# while i < n:
#     i += 2
#     evenSum += i
#     print("even num =", i)

# print("Total =", evenSum)

# 8. Write a python program to find sum of all odd numbers between 1 to n.

# n = int(input("Enter number: "))

# i = 1

# while i <= n:
#     print(i)
#     i += 2

# 9. Write a python program to print multiplication table of any number.

# n = int(input("Enter Table: "))

# i = 1

# while i <= 10:
#     print(f"{n} * {i} = {n * i}")
#     i += 1

# 10. Write a python program to count number of digits in a number.

# n = int(input("Enter Number to find length: "))

# l = 0

# while n != 0:
#     n //= 10
#     print(n)
#     l += 1

# print(l)

# 11. Write a python program to find first and last digit of a number.

# n = int(input("Enter Number to find length: "))

# f = 0
# l = 0
# i = 0

# while n != 0:
#     i += 1
#     if i == 1:
#         l = n % 10
#     elif n >= 1:
#         f = n
#     n //= 10

# print(l, "l")
# print(f, "f")


# print(4123 // 10)
# print(412 // 10)
# print(41 // 10)
# print(4 // 10)
