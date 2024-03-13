# print(5 / 0)
# print(a)
# print(34 + "HELLO")

# try:
#     # print(5 / 0)
#     # print("a")
#     print(34 + "HELLO")
# except ZeroDivisionError:
#     print("you can't did by zero")
# except NameError:
#     print("please check your variable declaration")
# except Exception as e:
#     print("something went wrong", e)
#     # raise Exception("created exception")
# else:
#     print("it is working without errors")
# finally:
#     print("done")


age = -5

if age >= 18:
    print("you can vote")
elif age <= 0:
    raise Exception("invalid")
else:
    print("you cannot vote")
