class Vector:
    def __init__(self, a, b):
        self.first_element = a
        self.second_element = b
    
    def __eq__(self, vector):
        if not (self.first_element == vector.first_element and self.second_element == vector.second_element):
            return False
        return True
    
    def __repr__(self):
        return f"Vector({self.first_element},{self.second_element})"

    def __add__(self, vector):
        new_first_element = self.first_element + vector.first_element
        new_second_element = self.second_element + vector.second_element
        return Vector(new_first_element, new_second_element)
    
    def __sub__(self, vector):
        new_first_element = self.first_element - vector.first_element
        new_second_element = self.second_element - vector.second_element
        return Vector(new_first_element, new_second_element)
    
    def __mul__(self, vector):
        new_first_element = self.first_element * vector.first_element
        new_second_element = self.second_element * vector.second_element
        return new_first_element + new_second_element

v1 = Vector(3, 4)
v2 = Vector(-4,5)
v3 = Vector(3, 4)

v4 = v1 + v2
v5 = v2 - v1
v6 = v1 * v2

print(repr(v1))
print(v3 == v1)
print(v4, v5, v6)
print(isinstance(v5, Vector))