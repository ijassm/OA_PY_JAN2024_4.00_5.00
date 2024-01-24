# 1. Write a program in python to display the first 10 natural numbers.
# Expected Output :
# 1 2 3 4 5 6 7 8 9 10


# for i in range(1, 11):
#     print(i)


# 2. Write a python program to compute the sum of the first 10 natural numbers.
# Expected Output :
# The first 10 natural number is :
# 1 2 3 4 5 6 7 8 9 10
# The Sum is : 55

# n = 10
# s = 0

# for i in range(1, n + 1):
#     # s = s + i
#     s += i

# print("The Sum is :", s)


# 3. Write a program in python to display n terms of natural numbers and their sum.
# Test Data : 7
# Expected Output :
# The first 7 natural number is :
# 1 2 3 4 5 6 7
# The Sum of Natural Number upto 7 terms : 28

# n = 7
# s = 0

# for i in range(1, n + 1):
#     s += i

# print(f"The Sum of Natural Number upto {n} terms: {s}")


# 4. Write a program in python to read 10 numbers from the keyboard and find their sum and average.
# Test Data :
# Input the 10 numbers :
# Number-1 :2
# ...
# Number-10 :2
# Expected Output :
# The sum of 10 no is : 55
# The Average is : 5.500000


# n = 10
# s = 0

# for i in range(1, n + 1):
#     s += int(input(f"Number-{i}: "))

# print(f"The Sum of Natural Number upto {n} terms: {s}")
# print(f"The Average is : {s / n}")


# 5. Write a program in python to display the cube of the number up to an integer.
# Test Data :
# Input number of terms : 5
# Expected Output :
# Number is : 1 and cube of the 1 is :1
# Number is : 2 and cube of the 2 is :8
# Number is : 3 and cube of the 3 is :27
# Number is : 4 and cube of the 4 is :64
# Number is : 5 and cube of the 5 is :125

# terms = int(input("Input number of terms : ")) + 1

# for i in range(1, terms):
#     print(f"Number is : {i} and cube of the {i} is : {i**3}")


# 6. Write a program in python to display the multiplication table for a given integer.
# Test Data :
# Input the number (Table to be calculated) : 15
# Expected Output :
# 15 X 1 = 15
# ...
# ...
# 15 X 10 = 150

# table = int(input("Table to be calculated : "))
# step = 10 + 1

# for i in range(1, step):
#     print(f"{table} X {i} = {table * i}")


# 7. Write a program in python to display the multiplier table vertically from 1 to n.
# Test Data :
# Input upto the table number starting from 1 : 8
# Expected Output :
# Multiplication table from 1 to 8
# 1x1 = 1, 2x1 = 2, 3x1 = 3, 4x1 = 4, 5x1 = 5, 6x1 = 6, 7x1 = 7, 8x1 = 8
# ...
# 1x10 = 10, 2x10 = 20, 3x10 = 30, 4x10 = 40, 5x10 = 50, 6x10 = 60, 7x10 = 70, 8x10 = 80

# table = int(input("Tables upto : "))
# time = int(input("Times upto : "))
# loops = (table * time) + 1

# step = 0
# loopTable = 1

# print(loops)

# for i in range(1, loops):
#     step += 1
#     print(f"{loopTable} x {step} = {loopTable * step}")
#     if step % time == 0:
#         step = 0
#         loopTable += 1
#         print()


# website link : https://www.w3resource.com/c-programming-exercises/for-loop/index.php