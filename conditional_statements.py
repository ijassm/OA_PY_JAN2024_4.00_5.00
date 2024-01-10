# age = int(input("enter your age: "))

# if age >= 18:
#     print("you can vote")
# elif age <= 0:
#     print("invalid")
# else:
#     print("you cannot vote")

a = 10
b = 40
c = 30

if a > b and a > c:
    print(f"a is greater {a}")
    if b < c:
        print(f"b is smallest {b}")
    else:
        print(f"c is smallest {c}")
elif b > a and b > c:
    print(f"b is greater {b}")
    if a < c:
        print(f"a is smallest {a}")
    else:
        print("c is smallest", c)
else:
    print("c is greater", c)
    if a < b:
        print("a is smallest", a)
    else:
        print("b is smallest", b)
