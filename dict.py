# no index
# ordered
# it will be in key : value order

# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York",
#     "skills": ["PY", "JAVA", "JS", "DART"],
#     "address": "New York, NY, USA",
# }

# personList = ["John", 30, "New York"]


# print(person)
# print(person["name"])
# print(person["age"])
# print(person["city"])
# print(person["skills"])
# print(type(person))


# person["address"] = "Pondy"
# person.update({"address": "Pondy"})

# print(person)


# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {"e": 5, "c": 3, "a": 1, "d": 4, "b": 2}
items = []

# print(d.keys())
# print(d.values())

for i in d:
    items.append((i, d[i]))

print(items, "original value")
length = len(items)

for i in range(length):
    for j in range(i + 1, length):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

print(items, "ascending value")
