money = int(input("enter your amount to get change: "))

Rs2000 = Rs500 = Rs200 = Rs100 = Rs50 = Rs20 = Rs10 = Rs5 = Rs2 = Rs1 = 0

# example
# money = 4623

if money >= 2000:
    Rs2000 = money // 2000
    money %= 2000

if money >= 500:
    Rs500 = money // 500
    money %= 500

if money >= 200:
    Rs200 = money // 200
    money %= 200

if money >= 100:
    Rs100 = money // 100
    money %= 100

if money >= 50:
    Rs50 = money // 50
    money %= 50

if money >= 20:
    Rs20 = money // 20
    money %= 20

if money >= 10:
    Rs10 = money // 10
    money %= 10

if money >= 5:
    Rs5 = money // 5
    money %= 5

if money >= 2:
    Rs2 = money // 2
    money %= 2

if money >= 1:
    Rs1 = money // 1
    money %= 1


print("Total number of notes: ")
print(f"Rs 2000 - {Rs2000} notes")
print(f"Rs 500  - {Rs500} notes")
print(f"Rs 200  - {Rs200} notes")
print(f"Rs 100  - {Rs100} notes")
print(f"Rs 50   - {Rs50} notes")
print(f"Rs 20   - {Rs20} notes")
print(f"Rs 10   - {Rs10} notes")
print(f"Rs 5    - {Rs5} notes")
print(f"Rs 2    - {Rs2} notes")
print(f"Rs 1    - {Rs1} notes")


# overview of program

# Rs2000 => 2 Notes r = 623
# Rs500 => 1 Note r = 123
# Rs100 => 1 Note r = 23
# Rs20 => 1 Note r = 3
# Rs2 => 1 Note r = 1
# Rs1 => 1 Note r = 0
