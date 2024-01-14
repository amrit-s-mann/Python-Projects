import math

class Polygon:
    def get_area(self):
        raise NotImplementedError("You must implement the 'get_area' method")

    def get_sides(self):
        raise NotImplementedError("You must implement the 'get_sides'method")
    
    def get_perimeter(self):
        return sum(self.get_sides())

class Triangle(Polygon):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def get_sides(self):
        sides = [self.side_1, self.side_2, self.side_3]
        return sides
    
    def get_area(self):
        triangle_area = get_triangle_area(self.side_1, self.side_2, self.side_3)
        return triangle_area

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        sides = [self.width, self.height, self.width, self.height]
        return sides
    
    def get_area(self):
        rectangle_area = get_rectangle_area(self.width, self.height)
        return rectangle_area

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        super().get_sides()
        super().get_area()

    def get_sides(self):
        return super().get_sides()

def get_triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    return math.sqrt(
        semi_perimeter *
        (semi_perimeter - side1) *
        (semi_perimeter - side2) *
        (semi_perimeter - side3)
    )

def get_rectangle_area(width, height):
    return width * height
