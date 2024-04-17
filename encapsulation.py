# # Python program for demonstrating protected members


# # first, we will create the base class
# class Base1:
#     def __init__(self):

#         # the protected member
#         self._p = 78


# # here, we will create the derived class
# class Derived1(Base1):
#     def __init__(self):

#         # now, we will call the constructor of Base class
#         Base1.__init__(self)
#         print("We will call the protected member of base class: ", self._p)

#         # Now, we will be modifing the protected variable:
#         self._p = 433
#         print("we will call the modified protected member outside the class: ", self._p)


# obj_1 = Derived1()

# obj_2 = Base1()

# # here, we will call the protected member
# # this can be accessed but it should not be done because of convention
# print("Access the protected member of obj_1: ", obj_1._p)

# # here, we will access the protected variable outside
# print("Access the protected member of obj_2: ", obj_2._p)


class Base1:
    def __init__(self):
        self.p = "Javatpoint"
        self.__q = "Javatpoint1"
        print(self.__q)


# Creating a derived class
class Derived1(Base1):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base1.__init__(self)
        print("We will call the private member of base class: ")
        print(self.__q)


# Driver code
obj_1 = Base1()
# obj_2 = Derived1()

# print(obj_1.p)
# print(obj_1.__q)

# print(obj_2.__q)
