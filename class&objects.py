class Person:
    firstName = None
    lastName = None
    age = None
    location = None

    def getDetails(self):
        print(self)
        print("FullName : ", self.firstName + " " + self.lastName)
        print("Age : ", self.age)
        print("Location : ", self.location)
        print()


# Creating a new Person object
obj1 = Person()
obj2 = Person()


obj1.firstName = "John"
obj1.lastName = "Doe"
obj1.age = 20
obj1.location = "Chennai"

obj2.firstName = "XYZ"
obj2.lastName = "ABC"
obj2.age = 20
obj2.location = "Pondy"


print(obj1)
# print(obj2)

obj1.getDetails()
obj2.getDetails()
