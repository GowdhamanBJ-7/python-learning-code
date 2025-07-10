from abc import ABC, abstractmethod
# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        print('area')

# Concrete class 1
class Circle(Shape):
    def area(self):
        print("Area of Circle")

# Concrete class 2
class Square(Shape):
    def area(self):
        print("Area of Square")

# Usage
shapes = [Circle(), Square()]
for shape in shapes:
    shape.area()
