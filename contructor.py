class Person:
    def __init__(self, firstName, lastName, age, location):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.location = location

    def getDetails(self):
        print(self)
        print("FullName : ", self.firstName + " " + self.lastName)
        print("Age : ", self.age)
        print("Location : ", self.location)
        print()


# Creating a new Person object
obj1 = Person("John", "Doe", 20, "chennai")
obj2 = Person("XYZ", "ABC", 25, "Pondy")


# obj1.firstName = "John"
# obj1.lastName = "Doe"
# obj1.age = 20
# obj1.location = "Chennai"

# obj2.firstName = "XYZ"
# obj2.lastName = "ABC"
# obj2.age = 20
# obj2.location = "Pondy"


# print(obj1)
# print(obj2)

obj1.getDetails()
obj2.getDetails()
