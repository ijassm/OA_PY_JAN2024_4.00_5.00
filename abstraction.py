from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def mileage(self):
        pass


class Ford(Car):

    def mileage(self):
        return "12kmph"


class Tesla(Car):

    def mileage(self):
        return "5kmph"


obj1 = Ford()


print(obj1.mileage())
