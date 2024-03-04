def recursiveFactorial(a):
    if a == 0:
        return 1
    else:
        return a * recursiveFactorial(a - 1)


print(recursiveFactorial(5))


# def factorial(a):
#     f = 1
#     for i in range(1, a + 1):
#         f *= i
#     return f


# print(factorial(5))

# Testcases
# sum(2)() = > 2
# sum(2)(4)() = > 6
# sum(2)(4)(4)() = > 10
# sum(2)(4)(4)(2)() = > 12
