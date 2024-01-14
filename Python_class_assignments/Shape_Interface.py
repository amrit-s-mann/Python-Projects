import math

class ShapeInterface:
    def get_area(self):
        raise NotImplementedError()
    
    def get_perimeter(self):
        raise NotImplementedError()
    
class Square(ShapeInterface):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def get_area(self):
        area = (self.side_length ** 2)
        print(area)
    
    def get_perimeter(self):
        perimeter = 4 * self.side_length
        print(perimeter)
    
class Circle(ShapeInterface):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = round(math.pi, 2) * (self.radius ** 2)
        print(area)
    
    def get_perimeter(self):
        perimeter = 2 * round(math.pi, 2) * self.radius
        print(perimeter)
    
def calculate(shape : ShapeInterface):
    shape.get_area()
    shape.get_perimeter()

square = Square(2)
circle = Circle(3)

calculate(square)
calculate(circle)

