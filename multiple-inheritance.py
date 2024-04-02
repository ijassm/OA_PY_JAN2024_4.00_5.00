# Multiple inheritance


# Base Class 1
class Calculation1:
    def summation(self, a, b):
        return a + b


# Base Class 2
class Calculation2:
    def multiplication(self, a, b):
        return a * b


# Base Class 3
class Calculation3:
    def subraction(self, a, b):
        return a - b


# Base Class 3
class Calculation4:
    def subraction(self, a, b):
        return a - b


# Derived Class
class Derived(Calculation1, Calculation2, Calculation3):
    def divide(self, a, b):
        return a / b


d = Derived()
print(d.summation(10, 20))
print(d.multiplication(10, 20))
print(d.subraction(10, 20))
print(d.divide(10, 20))


# issubclass(sub,sup) method

"""
The issubclass(sub, sup) method is used to check the relationships between the 
specified classes. It returns true if the first class is the subclass of the 
second class, and false otherwise.
"""

print(issubclass(Derived, Calculation1))
print(issubclass(Derived, Calculation2))
print(issubclass(Derived, Calculation3))
print(issubclass(Derived, Calculation4))

print(isinstance(d, Derived))
print(isinstance(d, Calculation1))
print(isinstance(d, Calculation2))
print(isinstance(d, Calculation3))
print(isinstance(d, Calculation4))
