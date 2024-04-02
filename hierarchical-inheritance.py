# Hierarchical Inheritance

# Hierarchical inheritance involves multiple inheritance from the same base or parent class.


class Parent:
    def func1(self):
        print("this is function 1")


class Child1(Parent):
    def func2(self):
        print("this is function 2")


class Child2(Parent):
    def func3(self):
        print("this is function 3")


obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()

obj2.func1()
obj2.func3()
