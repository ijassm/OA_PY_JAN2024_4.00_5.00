# Parent class
class Animal:
    def speak(self):
        print("Animal Speaking")


# child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")


# creating new object
d = Dog()

d.bark()
d.speak()
