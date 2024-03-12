# print(5 / 0)
# print(a)
# print(34 + "HELLO")

try:
    print(5 / 0)
    # print("a")
except ZeroDivisionError:
    print("you can't did by zero")
except NameError:
    print("something went wrong")
else:
    print("it is working without errors")
finally:
    print("done")
