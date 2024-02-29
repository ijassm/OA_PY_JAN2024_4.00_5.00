# def sum(a, b):
#     return a + b


# print(sum(1, 2))

# print(sum(1, 2, 3))

# Arbitrary Arguments, *args


# def sum(*n):
#     s = 0
#     for i in n:
#         s += i
#     return s


# print(sum(1, 2))

# print(sum(1, 2, 3))

# print(sum(23, 1, 2, 3))

# Keyword Arguments

# def person(name, age, location):
#     print(f"{name} is {age} years old and lives in {location}")


# person(20, "pondy", "john")

# person(age=20, location="pondy", name="John")

# Arbitrary Keyword Arguments, **kwargs


# def person(**person):
#     # print(person)
#     print("This person name is " + person["name"])
#     print(f"This person age is {person["age"]}")
#     print("This person current location is " + person["location"])
#     print("This person is" , "working" if person["working"] else "not working")
#     print()
#     # print(f"{name} is {age} years old and lives in {location}, and {working}")


# # person(20, "pondy", "john")

# person(age=20, location="pondy", name="John", working=False)
# person(age=20, location="pondy", name="John", working=True)


# Defualt Parameters


# def person(name, age, location="chennai"):
#     print(f"{name} is {age} years old and lives in {location}")


# person("John", 20, "Pondy")
# person("XYZ", 24)
