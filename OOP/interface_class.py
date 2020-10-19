# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(Shape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{ \" Circle\": {str(self.calcArea())} }}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())