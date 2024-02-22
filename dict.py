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

# d = {"e": 5, "c": 3, "a": 1, "d": 4, "b": 2}
# items = []

# # print(d.keys())
# # print(d.values())

# for i in d:
#     items.append((i, d[i]))

# print(items, "original value")
# length = len(items)

# for i in range(length):
#     for j in range(i + 1, length):
#         if items[i][1] > items[j][1]:
#             items[i], items[j] = items[j], items[i]

# print(items, "ascending value")


# 2 Convert two lists into a dictionary

# keys = ["Ten", "Twenty", "Thirty"]
# values = [10, 20, 30]

# new_dict = {}

# value_length = len(values)
# key_length = len(keys)

# if value_length == key_length:
#     for i in range(value_length):
#         key = keys[i]
#         value = values[i]
#         new_dict[key] = value
#     print(new_dict)
# else:
#     print("keys and values must be equal")

# 3. Merge two Python dictionaries into one

# dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
# dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}


# for i in dict2:
#     dict1[i] = dict2[i]

# print(dict1)


# 4. Print the value of key ‘history’ from the below dict

# sampleDict = {
#     "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
# }


# print(sampleDict)
# print(sampleDict["class"])
# print(sampleDict["class"]["student"])
# print(sampleDict["class"]["student"]["marks"])
# print(sampleDict["class"]["student"]["marks"]["history"])

# 5. Initialize dictionary with default values

# employees = ["Kelly", "Emma", "John"]
# defaults = {"designation": "Developer", "salary": 8000}

# output = {}

# output[employees[0]] = defaults
# {'kelly' : {"designation": "Developer", "salary": 8000}}
# output[employees[1]] = defaults
"""
{
'kelly' : {"designation": "Developer", "salary": 8000},
'Emma' : {"designation": "Developer", "salary": 8000}
}
"""
# for i in employees:
#     output[i] = defaults

# print(output)

# 6. Create a dictionary by extracting the keys from a given dictionary

# sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# # Keys to extract
# keys = ["name", "salary", "city"]

# output = {}

# for key in sample_dict:
#     for i in keys:
#         if key == i:
#             output[key] = sample_dict[key]
#             break

# print(output)

# 7. Python – Key with maximum unique values
# Given a dictionary with a values list, extract the key whose value has the most unique values.

# test_dict = {
#     "Gfg": [5, 7, 9, 4, 0],
#     "is": [6, 7, 4, 3, 3, 2, 1, 8],
#     "the": [6, 7, 4, 3, 3, 2, 1, 8],
#     "good": [9, 9, 6, 5, 5],
# }

# maxValue = 0
# maxKey = []

# for i in test_dict:
#     if len(set(test_dict[i])) > maxValue:
#         maxValue = len(set(test_dict[i]))
#         maxKey.append(i)

# print(maxKey, maxValue)
# print(test_dict)
