# Using Abstract Base Classes to enforce class constraints

from abc import ABC, abstractmethod


class Shape(ABC):
    # Inheriting from ABC indicates that this is an abstract base class
    def __init__(self):
        super().__init__()

    # declaring a method as abstract requires a subclass to implement it
    @abstractmethod
    def calcArea(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# Abstract classes instantiation gives an error
# g = Shape() # error

c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())